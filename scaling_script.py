#! /usr/local/bin/python

import requests
import subprocess
import time

def get_load_metrics():
    #response = requests.get('http://prometheus:9090/api/v1/query?query=rate(flask_http_request_total[1m])')
    response = requests.get('http://localhost:9090/api/v1/query?query=rate(flask_http_request_total[1m])')
    data = response.json()
    print(data)
    # You would parse the data and return the load or a boolean indicating if scaling is needed
    return data

def scale_service(service_name, scale_to):
    subprocess.run(['docker-compose', 'scale', f'{service_name}={scale_to}'])
    # for docker swarm
    #subprocess.run(['docker', 'service', 'update', '--replicas', str(scale_to), service_name])

try:
    metrics = get_load_metrics()
    load = metrics['data']['result'][0]['value'][1]
except IndexError as e:
    print("Error accessing data:", e)
    print("Metrics data received:", metrics)

# Example logic for scaling
if float(load) > 100:  # Threshold should be adjusted based on your needs
    scale_service('web', 3)  # Scale up to 3 instances
    time.sleep(180)
elif float(load) < 10:
    scale_service('web', 1)  # Scale down to 1 instance