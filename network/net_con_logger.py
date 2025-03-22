import time
import sys
from datetime import datetime
import platform
import ping3

def ping(host='8.8.8.8'):
    try:
        response = ping3.ping(host, timeout=2)
        return response is not None
    except Exception:
        return False

def log_outage(start_time, end_time):
    duration = end_time - start_time
    with open("outage_log.txt", "a") as log_file:
        log_file.write(f"Outage Start: {start_time}, End: {end_time}, Duration: {duration}\n")
        print(f"Outage Start: {start_time}, End: {end_time}, Duration: {duration}\n")

def monitor_connection():
    outage_start = None
    while True:
        if not ping():
            now = datetime.now()
            if outage_start is None:
                outage_start = now
                with open("outage_log.txt", "a") as log_file:
                    log_file.write(f"Internet Down: {now}\n")
                    print(f"Internet Down: {now}\n")
        else:
            if outage_start is not None:
                log_outage(outage_start, datetime.now())
                outage_start = None
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_connection()