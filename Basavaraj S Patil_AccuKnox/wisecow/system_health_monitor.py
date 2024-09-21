import psutil
import time
import logging

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    
    # Check memory usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_info.percent}%")

    # Check disk usage
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > 90:
        logging.warning(f"High Disk usage detected: {disk_info.percent}%")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(60)  # Check every minute
