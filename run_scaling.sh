#!/bin/bash

# Loop indefinitely
while true; do
    /usr/bin/python3 ./scaling_script.py

    # Wait for 30 seconds before running again
    sleep 30
done