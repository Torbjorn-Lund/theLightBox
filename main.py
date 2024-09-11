"""
This is the main document for the LED matrix project
"""

# Importing required modules
from machine import Pin
import time
import machine
import _thread
import ujson as json
import gc # Garbage collector for memory management
import sys

# Importing custom modules
from lib.internett import Server_functiones, Access_point, get_location_inf, get_weather_data
from lib.lightbox_functionality import my_lightbox
from lib.encryption import Simple_Encryption
import lib.NTPtime as ntp 
from lib.pico_system import get_json_data, get_files, delete_file, save_json_data
import events as ev

# Hardware setup
button_pin = Pin(15, Pin.IN, Pin.PULL_DOWN) # Pin for physical button
reset_button_pin = Pin(0, Pin.IN, Pin.PULL_UP) # Pin for reset button

# Constants for button behavior
LONG_PRESS_TIME = 5000 # 5 seconds
DEBOUNCE_TIME = 50  # Debounce time in milliseconds
press_start_time = 0
press_start_time2 = 0
debounce_time = 100
core0_task = 2

def start_event_loop():
    """ 
    Function to start the event loop 
    This function continuously runs event_loop() from the events module
    """
    while True:
        try:
            my_lightbox.clear() # Clear buffer
            loop = ev.event_loop()
            if loop == "button_count_error":
                my_lightbox.button_count = 1 # Reset button count on error
            time.sleep(1)
            
        except Exception as e:
            print(f"ERR, an exception occurred: {e}")

def button_callback(pin):
    """ 
    Callback function for the physical button 
    This function handles button press and release events
    """
    global debounce_time, press_start_time

    if pin.value():
        press_start_time = time.ticks_ms() # Record button press start time
    else:
        if (time.ticks_ms()-debounce_time) > 500:
            press_duration = time.ticks_ms() - press_start_time # Calculates the time the button has been pressed

            # Long press action
            if press_duration > LONG_PRESS_TIME:
                print("Entering sleep mode")
                my_lightbox.set_button_count(0)
                my_lightbox.clear()
                my_lightbox.show()


            # Normal press action
            else:
                my_lightbox.change_button_count(1)
            
        debounce_time=time.ticks_ms()
        
def reset_button_callback(pin):
    """ 
    Callback function for reset button 
    This function handles reset button press and initiates system reset if pressed for a long duration
    """
    global press_start_time2, LONG_PRESS_TIME, DEBOUNCE_TIME

    current_time = time.ticks_ms()
    
    # Check if button is pressed (assuming active low) and debounce
    if pin.value() == 0 and time.ticks_diff(current_time, press_start_time2) > DEBOUNCE_TIME:
        press_start_time2 = current_time  # Record the current time
        print("Button press detected, start timing...")

    # If pressed for required duration, perform system reset
    if time.ticks_diff(current_time, press_start_time2) >= LONG_PRESS_TIME:
        print("Button held for 5 seconds, initiating reset process...")
        temp_obj = Server_functiones("","")
        temp_obj.close_server()
        print("Server stopped")
        my_lightbox.run = False
        my_lightbox.minute = 0

        my_lightbox.clear()
        print("All stopped")
        reset()

def get_internet_credentials() -> tuple:
    """ 
    Retrieve Wi-Fi credentials from encrypted JSON file 
    Returns:
        Tuple containing Wi-Fi SSID and password
    """
    filepath = 'data/config.json'
    encoder = Simple_Encryption()
    with open('data/setup.json', 'r') as f:
        key = json.load(f)['key'].encode()
    
    # Get data
    data = encoder.load_encrypted_json(filepath, key)

    # If an error occurred
    if data == None:
        return None, None
    
    # Formating
    wifi_name = data['wifi_credentials']['SSID'].encode('utf-8')
    wifi_password = data['wifi_credentials']['PASSWORD'].encode('utf-8')
    wifi_name = wifi_name.decode('utf-8')
    wifi_password = wifi_password.decode('utf-8')

    if wifi_name == "" or wifi_password == "":
        return None, None
    else:
        return wifi_password, wifi_name
    
def reset():
    """ 
    Reset system to factory settings and restart lightbox 
    - Clear Wi-Fi credentials
    - Reset setup data
    - Delete images in image folder
    - Restart system
    """
    print("detected")
    # Create empty object
    temp_obj = Access_point("","")

    # Clear wifi password and SSID
    temp_obj.save_form_data("","")

    print("wifi parameters have been reset")
    
    # Reset setup parameters
    json_data = get_json_data("data/setup_backup.json")
    save_json_data(json_data, "data/setup.json")
    print("default parameters set")

    # Delete all image files
    files = get_files("images", "ppm")
    for file in files:
        print(file)
        delete_file(f"images/{file}")
    print("all files have been deleted")
    time.sleep(1)
    print("restarting")
    # Reset machine
    machine.reset()

def update_system_data():
    """
    Function updates system information
    This includes:
        - Location based on IP
        - Localtime
        - Weater data
    """
    with open("data/setup.json", "r") as json_file:
        json_data = json.load(json_file)
    
    # If the file is missing information, get information
    if json_data["location"] == {}:
        print("location")
        get_location_inf() # Set location based on IP address
        time.sleep(1) # Waiting for program to close
    print("time")
    ntp.set_time() # Set RTC time
    print("weather")
    get_weather_data() # Fetch weather data

def main():
    global core0_task
    """
    Main loop, this is where the program start

    """
    min_mem_free_update = 70000 # Minimum avelitable memory to update weather
    # Try/except/finnaly for error handling 
    try:
        print("Initializing startup proces...")

        reset_button_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=reset_button_callback) # Reset button interrupt
        my_lightbox.show_loading_bar(5,(255,255,255),animation=True) 
        internet_credentials = get_internet_credentials()

        # If internet credentiales have not been registered
        if (internet_credentials == (None, None) or internet_credentials == ("", "")):
            
            # Display on matrix
            my_lightbox.clear()
            my_lightbox.setFig_wifi((255,0,0))

            #print("Starting access point")
            ap = Access_point("My Lightbox wifi setup", "lightbox") # Create object
            # Opens an access point
            ap_return = ap.handle_request()
            if ap_return == "err":
                print("An error occurred, restarting")
                machine.reset()

            # When done
            my_lightbox.clear()
            my_lightbox.setFig_wifi((0,255,0))
            ap.sock.close()  # Unbind the socket and release resources
            del ap # Freeing resources

            # Waiting for program to close
            time.sleep(3)

            my_lightbox.clear() 
            my_lightbox.show_loading_bar(6,(255,255,255),animation=True) # Progress bar

            # Get internet credentiales
            internet_credentials = get_internet_credentials()

            my_lightbox.show_loading_bar(7,(255,255,255),animation=False) # Progress bar
        
        # Sets interrupt for button presses, do not want the timed interrupts to be at the same time
        button_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_callback)
        # You can stop the RTC timer with the following code:
        # rtc_timer.deinit()

        my_lightbox.show_loading_bar(16,(255,255,255),speed=0.1,animation=True) # Progress bar
        my_lightbox.clear() # Clearing screen

        # Start task on core_1, run through the event loop
        _thread.start_new_thread(start_event_loop, ())

        # Create an instance of internett object
        password, name = internet_credentials
        lightbox_internett = Server_functiones(name, password)

        hostname = get_json_data("data/setup.json")["hostname"] 
        connection_ok = lightbox_internett.connect_internett(hostname)
        
        # Keep trying to connect to internet
        while connection_ok != True:
            connection_ok = lightbox_internett.connect_internett(hostname)
            time.sleep(3)
        
        # Define a function to be used as a callback for the timer
        def close_server_callback(timer):
            """ Callback function. Stop server and set task=2 """
            global core0_task
            lightbox_internett.run = False
            core0_task = 2
        
        # Set interrupt
        rtc_timer = machine.Timer(-1)
        rtc_timer.init(period=1800000, mode=machine.Timer.PERIODIC, callback=close_server_callback) # every hour. Close the server so the program can move forwoard. 3600000ms=1hour... 1800000
        
        # Event loop fore core0. Should never exit this loop.
        # Every half an hour a timer runs out, canceling the current task and changing the task number.
        counter = 1
        while True:
            try:
                # Run server
                if core0_task == 1:
                    lightbox_internett.run = True
                    lightbox_internett.start_server()
                # Update system information
                elif core0_task == 2:

                    gc.collect() # Trigger garbage collector

                    if gc.mem_free() > min_mem_free_update:
                        if counter == 0:
                            # Update weather data
                            get_weather_data()
                            counter = 1
                        else:
                            print("Update started")
                            update_system_data() # Update all system data
                            counter = 2
                        
                        # Reset core task
                        core0_task = 1
                        print("Update done")
                        
                    else:
                        #print("not enough:", gc.mem_free())
                        time.sleep(3)

                    time.sleep_ms(1)

            # If an error occure
            except Exception as e:
                print(f"An error occured: {e}")
                time.sleep(3)

    # In the case of an error
    except Exception as e:
        print(f"An error occurred: {e} - Device restarting")
        max_lines = 20

        # Getting data
        with open("data/logg.txt", "r") as file:
            data = file.read()

        data = data.split("\n")

        # Checking length
        if len(data) > max_lines:
            data.pop(0)
        
        data.append(f"ERROR at {time.localtime()}: {e} - Device restarting")
            
        # Logging error
        with open("data/logg.txt", "w") as file:
            for line in data:
                if line != "":
                    file.write(line + "\n")

        time.sleep(1)
        machine.reset() # Reset device

# Calling the main loop
main()