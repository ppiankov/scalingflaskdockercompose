import requests
import subprocess
import time

# Constants
SCALE_DOWN_THRESHOLD = 0.1  # Load threshold below which to consider scaling down
SCALE_UP_THRESHOLD = 0.2    # Load threshold above which to consider scaling up
MINUTES_TO_CHECK = 2        # Duration to check for consistent load before scaling
LOAD_CHECK_INTERVAL = 30    # Script run interval in seconds
LOW_LOAD_COUNT_REQUIRED = MINUTES_TO_CHECK * (60 / LOAD_CHECK_INTERVAL)
HIGH_LOAD_COUNT_REQUIRED = MINUTES_TO_CHECK * (60 / LOAD_CHECK_INTERVAL)

# Global list to track load values
load_history = []

def get_load_metrics():
    response = requests.get('http://localhost:9090/api/v1/query?query=rate(http_requests_total[5m])')
    data = response.json()
    return data

def scale_service(service_name, scale_to):
    subprocess.run(['docker-compose', 'scale', f'{service_name}={scale_to}'], check=True)

def main():
    global load_history
    try:
        metrics = get_load_metrics()
        if metrics['data']['result']:
            current_load = float(metrics['data']['result'][0]['value'][1])
            print(f"Current Load: {current_load}")
            load_history.append(current_load)
        else:
            load_history.append(0)
    except Exception as e:
        print(f"Error fetching or parsing metrics: {e}")
        load_history.append(0)

    # Maintain only the relevant history length for the longest period required
    if len(load_history) > max(LOW_LOAD_COUNT_REQUIRED, HIGH_LOAD_COUNT_REQUIRED):
        load_history.pop(0)

    # Determine scaling action
    if len(load_history) >= LOW_LOAD_COUNT_REQUIRED and all(load < SCALE_DOWN_THRESHOLD for load in load_history):
        print("Scaling down due to low load...")
        scale_service('web', 1)
    elif len(load_history) >= HIGH_LOAD_COUNT_REQUIRED and all(load > SCALE_UP_THRESHOLD for load in load_history):
        print("Scaling up due to high load...")
        scale_service('web', 3)
    else:
        print("No scaling action taken.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(LOAD_CHECK_INTERVAL)
