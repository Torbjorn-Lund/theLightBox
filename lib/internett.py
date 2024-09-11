import network
import usocket as socket
from time import sleep, localtime
import uos
import ujson as json
import urequests as requests
import lib.pico_system as pSys
from lib.lightbox_functionality import my_lightbox
from encryption import Simple_Encryption
import weather as wd
import gc

def get_weather_data():
    """ Updates weather data from https://openweathermap.org/ """

    try:
        # Load JSON data
        json_data = pSys.get_json_data("data/setup.json")
        
        # Extract coordinates and other details
        lat = json_data["location"]["lat"]
        lon = json_data["location"]["lon"]
        units = json_data.get("units", "metric")  # Default to 'metric' if not specified
        API_key = json_data["openweathermap_api_key"]

    except KeyError as e:
        print(f"WARNING: {e} - getting data")
        get_location_inf()
        return "ERROR, key error"
    
    except Exception as e:
        print(f"Error getting weather data: {e}")
        return "ERROR, exception"

    # Normalize units
    if units == "celsius":
        units = "metric"
    elif units == "fahrenheit":
        units = "imperial"

    # Get data from API
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units={units}"

    try:
        response = requests.get(url).json()
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return "ERROR, fetch error"
    
    # Current time in ISO 8601 format
    iso8601_time = "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z".format(
        localtime()[0], localtime()[1], localtime()[2],
        localtime()[3], localtime()[4], localtime()[5]
    )

    # Save to dictionary
    weather_data = {
        "dt": iso8601_time,
        "symbol_code": response["weather"][0]["main"],
        "symbol_code_id": response["weather"][0]["icon"],
        "temp": response["main"]["temp"],
        "sunrise": response["sys"]["sunrise"],
        "sunset": response["sys"]["sunset"]
    }

    # Assign the weather data to the global or class variable
    wd.weather_data = weather_data

    # Trigger garbage collection to free up memory
    gc.collect()

def get_location_inf():
    """ Get information about location from "https://ip-api.com/" and saves data in "data/setup.json" """
    url = "http://ip-api.com/json/?fields=status,message,country,countryCode,lat,lon,timezone,offset,query"
    
    # Opens json file
    json_data = pSys.get_json_data("data/setup.json")
    
    # Request
    response = requests.get(url).json()

    # Adds new data
    json_data["location"] = {
        "lat": response["lat"],
        "lon": response["lon"],
        "timezone": response["timezone"],
        "timezone_offset": response["offset"],
        "countryCode": response["countryCode"]
    }

    # Save data
    pSys.save_json_data(json_data, "data/setup.json")

def set_default_setup_parameters() -> None: # ikke sikkert virker, må testes
    """ Set the lightbox back to default settings """

    json_data = pSys.get_json_data("data/setup_backup.json")
    pSys.save_json_data(json_data, "data/setup.json")
    sleep(1)

    get_location_inf()
    get_weather_data()   

class Access_point():
    def __init__(self, ssid:str, ap_password:str, ap_port:int=80) -> None:
        self.ssid = ssid
        self.ap_password = ap_password
        self.ap_port = ap_port
        self.sock = None

    def ap_init(self):
        """ Initializes an access point and sets up the socket. """
        done = False
        runtimes = 0
        max_try = 5
        sock = None
    
        # Configuring acces point
        ap = network.WLAN(network.AP_IF)
        ap.config(essid=self.ssid, password=self.ap_password) # slett passord?
        ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '0.0.0.0'))
        ap.active(True)

        # Try to bind the socket
        while not done and runtimes < max_try:
            try:
                # Create socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(('0.0.0.0', self.ap_port))
                sock.listen(5)
                done = True
                break
            except OSError as e:
                if e.errno == 98:
                    print("Port is already in use. Trying again...")
                    # Close the socket to unbind it
                    if sock:
                        sock.close()
                else:
                    print("An OSError occurred, returning:", e)
                    return "err"
            runtimes += 1

        # Set socket
        self.sock = sock
    
    def save_hostname(self, hostname:str):
        """ Save new host name. """
        #print("Setting new host name:", hostname)
        filepath = "data/setup.json"

        # Getting old data
        data = pSys.get_json_data(filepath)
        data["hostname"] = hostname

        # Overwriting old data
        pSys.save_json_data(data,filepath)

    def save_form_data(self, wifi_name:str, wifi_password:str):
        """ Encrypt and save data """

        filepath = 'data/config.json'
        encoder = Simple_Encryption()

        # Get key
        with open('data/setup.json', 'r') as f:
            key = json.load(f)['key'].encode()

        # Create a dictionary with the provided data
        new_data = {'SSID': wifi_name, 'PASSWORD': wifi_password}

        data = encoder.load_encrypted_json(filepath, key)

        if data == None:
            print("Not encrypted!")
            with open(filepath, "r") as f:
                data = json.load(f)

        # Adding the new data
        data['wifi_credentials'] = new_data
        encoder.save_encrypted_json(data, filepath, key)

    def handle_request(self):
            """Sets up an access point and handles incoming requests."""
            # Start access point
            sock = self.ap_init()
            run = True
            ip_displayed = False

            if sock == "err" or self.sock is None:
                print("returning err")
                return "err"

            while run:
                conn, addr = self.sock.accept()

                # Display IP on matrix only once
                if not ip_displayed:
                    my_lightbox.show_text("IP: 192.168.4.1", (255, 255, 255), 5, run_times=1)
                    ip_displayed = True

                try:
                    request = conn.recv(1024)
                    request_str = request.decode()

                    if 'POST' in request_str:
                        if '/internett' in request_str:
                            headers, body = request_str.split('\r\n\r\n', 1)
                            form_data = json.loads(body)

                            # Save the form data to a file
                            self.save_form_data(form_data['wifiName'], form_data['wifiPassword'])

                            # If the hostname is to be changed
                            if form_data["hostname"] != "mylightbox":
                                self.save_hostname(form_data["hostname"])

                            # Send response
                            conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<p>WIFI credentials successfully saved!</p>".encode())
                            self.close_connection(conn)
                            run = False
                    else:
                        # Open HTML
                        with open("web/wifi_credentials.html", "r") as file:
                            html = file.read()
                        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode() + html.encode())
                except Exception as e:
                    print(f"Unexpected exception: {e}")
                    conn.send("HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n<html><body>500 Internal Server Error</body></html>".encode())
                finally:
                    self.close_connection(conn)

    def close_connection(self, conn):
        if conn:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing socket: {e}")

class Pico_internet:
    """ 
    Class includes methods to control internet connection on a RP2040 board
    Have two attributes, internet name and password
    """
    def __init__(self, SSID:str, PASSWORD:str) -> None:
        """ Constructor """
        self.SSID = SSID
        self.PASSWORD = PASSWORD
        self.ip = None  # IP address of the device
        self.wlan = network.WLAN(network.STA_IF)
        self.connection = None

    def connect_internett(self, host_name:str="mylightbox") -> bool:
        """ Connects the raspberry to internett. Returns False if connection failed """
        
        self.wlan.active(True)
        network.hostname(host_name)  # Sets hostname
        self.wlan.connect(self.SSID, self.PASSWORD)
        max_wait = 60  # Try up to 60 times before quitting

         # Try to connect
        while not self.wlan.isconnected():
            max_wait -= 1
            print('Waiting for connection...')
            if max_wait < 0:  # Avoid running indefinitely
                print("Could not connect to the internet")
                return False
            sleep(1)

        self.ip = self.wlan.ifconfig()[0]
        print(f'Connected on {self.ip}')
        
        # Clean up
        gc.collect()
        
        return True
    
    def open_socket(self, port:int=80, max_conn:int=5):
        """ 
        Opens a socket.
        port: socket to be opened on
        max_conn: max queued connectiones
        """

        if not self.ip:
            print("IP address is not set. Connect to the internet first.")
            return None
        
        address = (self.ip, port)
        #self.connection = socket.socket()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        connection_ok = False
        max_try = 20

        # Runs until successful connection
        for i in range(max_try):
            try:
                self.connection.bind(address)
                self.connection.listen(max_conn)  # max queued connections
                connection_ok = True
                break
            except OSError as e:
                print(f"Error binding socket on attempt {i + 1}: {e}")
                self.connection.close()
                sleep(1)  # Add a delay before the next attempt

        if connection_ok:
            print("Socket opened")
            return self.connection
        else:
            print("Failed to open socket")
            return None
    
    def close_socket(self):
        """ Close the opened socket """
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Socket closed")
        
        # Clean up
        gc.collect()

OK_200 = "HTTP/1.1 200 OK\r\n"
NOT_FOUND_404 = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
INTERNAL_SERVER_ERROR_500 = "HTTP/1.1 500 Internal Server Error\r\n\r\n<h1>500 Internal Server Error</h1>"
BAD_REQUEST_400 = "HTTP/1.1 400 Bad Request\r\nContent-type: text/plain\r\n\r\nUnsupported request method"

class Server_functiones(Pico_internet):
    """
    This class includes functionalety for controlling the internet connection on a RP2040 board (only tested on a raspberry pi pico)
    and hosting a server

    - Use connect_internett() to connect to a internett
    - Use start_server() to start hosting a server
    """
    def __init__(self, SSID: str, PASSWORD: str) -> None:
        super().__init__(SSID, PASSWORD)
        self.run = False # Flag to control server running status
        self.max_image_files = 10
        self.current_socket = None
    
    """
    The folowing functiones are used to handle requests
    """
    def handle_client_headers(self, request_str) -> dict:
        """ Returns header data as a dictionary """
        return dict(line.split(': ', 1) for line in request_str.split("\r\n") if ':' in line)

    
    def construct_headers(self,status_code:str,content_type:str,content_length=None,access_control_allow_origin:str="*") -> str:
        """
        Returns header data

        status codes: 200 OK, 400 Bad Request
        content_type: 
        Access_Control_Allow_Origin: *=any origin
        """
        headers = f"HTTP/1.1 {status_code}\r\nContent-Type: {content_type}\r\n"
        if content_length is not None:
            headers += f"Content-Length: {content_length}\r\n"
        headers += f"Access-Control-Allow-Origin: {access_control_allow_origin}\r\n\r\n"
        return headers

    def read_and_send_chunks(self, filepath:str, client_socket, content_type:str, read_mode:str="r", chunk_size:int=1024, encode:bool=True, compressed=False):
        """ 
        Reads chunks of a file and sends them to the client on the fly. Useful when resources are limited 
        compressed - if the file is compressed, parameter should be set to compression type. For example, gzip.
        """
        
        headers = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n"
        if compressed != False:
            headers += f"Content-Encoding: {compressed}\r\n"  # Add Content-Encoding header
        headers += "\r\n"
        client_socket.send(headers.encode('utf-8'))

        with open(filepath, read_mode) as file:
            while chunk := file.read(chunk_size):
                if encode:
                    client_socket.send(chunk.encode('utf-8'))
                else:
                    client_socket.send(chunk)

    def send_in_chunks(self, client_socket, content, content_type:str, encode:bool=True, compressed=False):
        """ Sends data in chunks to client """
        chunk_size = 1024
        headers = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n"
        if compressed:
            headers += f"Content-Encoding: {compressed}\r\n"
        headers += "\r\n"
        client_socket.send(headers.encode('utf-8'))

        for i in range(0, len(content), chunk_size):
            chunk = content[i:i + chunk_size]
            if encode:
                chunk = chunk.encode('utf-8')
            client_socket.send(chunk)
    
    def _handle_options(self, client_socket, status_code="200 OK"):
        """ Responds with appropriate headers to allow the actual POST request. Access-Control-Allow-Origin: * header allows requests from any origin."""
        response = f'HTTP/1.1 {status_code}\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Methods: POST, OPTIONS\r\nAccess-Control-Allow-Headers: Content-Type\r\n\r\n'
        client_socket.send(response.encode('utf-8'))

    def extract_from_get(self,request):
        """ Extract information from request, sent over the url """

        query_string_start = request.find("?")
        if query_string_start != -1:
            query_string_end = request.find("HTTP/")
            query_string = request[query_string_start+1:query_string_end-1]
            query_list = query_string.split("&")
            dictionary = {}
            for item in query_list:
                key, value = item.split("=")
                dictionary[key] = value
            return dictionary
        else:
            return {"type": "unknown"}  

    def handle_get_settings(self, client_socket, request_data: dict) -> None:
        """ Handle get requests targetting settings """
        setup_data = pSys.get_json_data("data/setup.json") # Get current setup data
        
        # User requestet information about current setup
        if request_data["type"] == "inf":
            # Construct data
            if setup_data["manual_time_zone"] != False:
                setup_data["location"]["timezone_offset"] = setup_data["manual_time_zone"]
            json_data = json.dumps({"location":setup_data["location"],"units":setup_data["units"]})
            response = self.construct_headers("200 OK", "application/json") + json_data
            client_socket.send(response.encode('utf-8'))

        # User want to make a change to current setup
        elif request_data["type"] == "change":
            for key, value in request_data.items():
                if key in setup_data:
                    setup_data[key] = int(value) if value.isdigit() else value
                if key in setup_data["location"]:
                    setup_data["location"][key] = int(value) if value.isdigit() else value
            
            if "timezone_offset" in request_data:
                setup_data["manual_time_zone"] = int(request_data["timezone_offset"])
            if "brightness" in request_data:
                my_lightbox.change_brightness(int(request_data["brightness"]))
            self._handle_options(client_socket) # Allow Access-Control-Allow-Origin
            pSys.save_json_data(setup_data,"data/setup.json") # Saving new data
        
        # User want to restore default settings
        elif request_data["type"] == "revert":
            set_default_setup_parameters()
        else:
            client_socket.send(NOT_FOUND_404.encode('utf-8'))
            print("warning: requested data not found")

    def handle_get_images(self, client_socket, request_data: dict) -> None:
        """ Handle get requests targetting image data """
        image_folder_path = "/images"
        file_names = uos.listdir(image_folder_path) # Returns list with file names

        # Send filenames if user request "inf"
        if request_data["type"] == "inf":
            response = self.construct_headers("200 OK", "text/plain") + "\n".join(file_names)
            client_socket.send(response.encode('utf-8'))
        
        # If user want image data
        elif request_data["type"] == "data":
            if request_data["filename"] in file_names:
                image_data = pSys.get_data(f"{image_folder_path}/{request_data['filename']}")
                # Send header
                headers = self.construct_headers("200 OK", "image/x-portable-pixmap",len(image_data))
                client_socket.send(headers.encode('utf-8'))
                # Send file data
                data_send = image_data + "\r\n\r\n"
                client_socket.send(data_send.encode('utf-8'))
            # If requestet file does not exist
            else:
                client_socket.send(NOT_FOUND_404.encode('utf-8'))
                print("warning: requested data not found")

        # If user wants to delete image
        elif request_data["type"] == "del":
            if request_data["filename"] in file_names:
                pSys.delete_file(f"/images/{request_data['filename']}")
                self._handle_options(client_socket) # Allow Access-Control-Allow-Origin and status code OK
            else: # If file not found
                print("Warning, file not found")
                client_socket.send(NOT_FOUND_404.encode('utf-8'))

    def handle_get_event_pos(self, client_socket, request_data: dict) -> None:
        """ When client want to change event position (button count)"""
        try:
            increment = int(request_data["increment"])
            my_lightbox.change_button_count(increment)
            self._handle_options(client_socket) # Allow Access-Control-Allow-Origin and status code OK
        except ValueError as e:
            print(f"Warning, Unprocessable Entity: {e}")
            client_socket.send("HTTP/1.1 422 Unprocessable Entity".encode('utf-8'))

    def _handle_get(self, client_socket, request):
        """ Handle get requests """
        try:
            request_data = self.extract_from_get(request) # Split the client request into a dictionary
            if "settings" in request: # User want to acces settings
                self.handle_get_settings(client_socket, request_data)
            elif "images" in request: # User want to handle image data
                self.handle_get_images(client_socket, request_data)
            elif "event_pos" in request: # User want to change the event position (button count)
                self.handle_get_event_pos(client_socket, request_data)
            elif "refresh_weather" in request:
                get_weather_data()
                self._handle_options(client_socket)
            else: # If nothing of the above, send index
                html = pSys.get_data("web/index.html.gz","rb")
                self.send_in_chunks(client_socket, html, "text/html", encode=False, compressed="gzip") # Send gzipped HTML content in chunks
        except Exception as e:
            print(f"Exception occurred when handling get: {e}")
            client_socket.send(self.internal_server_error_500.encode('utf-8'))

    def _handle_post(self, chunk, filepath, status="read"):
        """ 
        Handle file upload
        """
        boundary = b'------WebKitFormBoundary'# 16 randome tall og bokstaver er etter

        if status == "read":
            boundary_index = chunk.find(boundary)
            # If boundary not found
            if boundary_index == -1:
                return (False, None)
            
            # If boundary found
            else:
                file_header, file_data = chunk.decode('utf-8').split("\r\n\r\n")
                file_header = file_header.split(";")

                # Extract filename
                for value in file_header:
                    if "filename=" in value:
                        # Extract the filename part and strip surrounding whitespace and quotes
                        filename = value.split('=')[1].split("\n")[0].strip()
                        filename = filename[1:-1] # gets rid of ""
                
                filepath += filename
                temp_filepath = filepath
                number = 1
                # Make unique file name
                while pSys.file_exists(temp_filepath):
                    temp_filepath = filepath[:-4] + f"({number})" + filepath[-4:] # Add number to filename
                    number += 1
                filepath = temp_filepath
                
                # Save file data
                pSys.save_data(file_data.encode('utf-8'),filepath,"wb")
                return (True,filepath)

        # If we are only to save the data
        elif status == "write":
            if boundary not in chunk:
                pSys.save_data(chunk,filepath,"ab")
            # If boundary is included, we do not want all
            else:
                chunk = chunk.decode('utf-8')
                pSys.save_data(chunk[:-len("\r\n------WebKitFormBoundaryp9YqWI0uwMIHwshf--\r\n")].encode('utf-8'),filepath,"ab")
                return "done" # All is done
            
            return (False,False)
        
        # Else
        return (False,None)
        
    def _handle_client_request(self, client_socket):
        """ Process the client request """
        if client_socket is None:
            print("returning")
            return
        
        # Set a timeout for the client socket
        client_socket.settimeout(5)  # 50 seconds timeout, adjust as needed endret!
       
        # Initialize variables
        request_type = None
        filepath_save_post = "/images/"
        chunks_is_comming = True
        post_status = "read"

        while chunks_is_comming:
            #print("Waiting for a client to connect...")

            # Recieve data in chunks
            chunk = client_socket.recv(2048)

            # If there is no more data to recieve
            if not chunk or chunk == "":
                #print("Client disconected")
                chunks_is_comming = False
                break
            
            # The request type have not been set
            if request_type == None:

                request = chunk.decode('utf-8')
                #client_data = self.handle_client_headers(request)

                #  if the server receives an OPTIONS request
                if request.startswith('OPTIONS'):
                    #print("OPTIONS request registered")
                    request_type = 'OPTIONS'
                    self._handle_options(client_socket)
                #  if the server receives an GET request
                elif request.startswith('GET'):
                    #print("GET request registerd")
                    request_type = 'GET'
                    chunks_is_comming = False
                    self._handle_get(client_socket, request)
                #  if the server receives an POST request
                elif request.startswith('POST'):
                    #print("POST request registerd")
                    request_type = 'POST'
                    # Check if we have too many images
                    if len(pSys.get_files(filepath_save_post, ".ppm")) >= self.max_image_files:
                        print("Warning, too many files saved on device")
                        # Send status headers to client
                        self._handle_options(client_socket, "507 Insufficient Storage")
                        break # If we are done, break out of loop
                    else:
                        self._handle_options(client_socket)
                # If none of the above, send error response
                else:
                    # Handle other types of requests or respond with an error
                    response = self.bad_request_400
                    client_socket.send(response.encode('utf-8'))
            
            # If the request is of the type "POST" the program wil seartch for a file and save the file localy
            if request_type == 'POST':
                handler = self._handle_post(chunk,filepath_save_post,post_status)

                # If boundery found=true, we now only want to save
                if handler[0] == True:
                    post_status = "write"
                    filepath_save_post = handler[1] # Change filepath
                elif handler == "done":
                    break # If we are done, break out of loop
                
    def close_server(self):
        """ Method is used to close the server """
        try:
            if self.current_socket != None:
                # Close the server socket
                self.current_socket.close()
                # Set run to False to stop the server
                self.run = False
            else:
                print("ERR, no server is running")
        except Exception as e:
            print(f"Error closing server: {e}")


    def start_server(self, port:int=80):
        """ Starts a web server """
        
        # Opens socket if necessary
        if self.current_socket == None:
            connection = self.open_socket(port)
            if connection == None:
                print("Could not start server")
                return
            else:
                self.current_socket = connection 
                self.current_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.current_socket.settimeout(3)

        # Resource cleanup
        connection = None
        
        # Runs the server until self.run is set to False
        while self.run == True:
            client_socket = None
            try:
                client_socket, address = self.current_socket.accept()
                print(f"Connection from {address}")
                self._handle_client_request(client_socket) # Process the client request

            # Error handling
            except OSError as e:
                if e.errno == 9:  # EBADF error
                    print(f"ERR1, [Errno 9] EBADF: {e} - When starting server")
                else:
                    if e.errno != 110: # This error wil occur naturaly (due to timeout), so we do not need to log it
                        print(f"Unexpected OSError: {e}")
            except Exception as e:
                print(f"Unexpected exception: {e}")
            finally:
                if client_socket:
                    client_socket.close()