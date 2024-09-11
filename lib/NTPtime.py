import machine
import ntptime
from lib.pico_system import get_json_data

def add_timezone_offset(timezone_offset: int) -> None:
    """ Add time offset to the RTC """

    # Get the current time from the RTC
    rtc = machine.RTC()
    year, month, day, weekday, hours, minutes, seconds, subseconds = rtc.datetime()

    # Apply timezone offset
    hours += timezone_offset // 3600
    minutes += (timezone_offset % 3600) // 60

    if minutes >= 60:
        minutes -= 60
        hours += 1
    if hours >= 24:
        hours -= 24
        day += 1

    # Set the adjusted time back to the RTC
    rtc.datetime((year, month, day, weekday, hours, minutes, seconds, subseconds))

def set_time() -> None:
    """ Sets the realtime clock to the time of the current position """
    
    # Get timezone offset
    json_data = get_json_data("data/setup.json")
    if json_data["manual_time_zone"] == False:
        delta = json_data["location"]["timezone_offset"]
    else:
        delta = json_data["manual_time_zone"]

    # Synchronize time with an NTP server
    ntptime.settime()
    
    # Set the RTC
    add_timezone_offset(delta)