#!/usr/bin/env python3

import json
import re
import time
import os
from alert_sender import send_alert

CONFIG_FILE = "config.json"

def load_config():
    """Loads configuration from config.json."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{CONFIG_FILE}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{CONFIG_FILE}'.")
        return None

def monitor_logs(config):
    """Monitors log files for error patterns."""
    if not config:
        return

    log_files = config.get("log_files", [])
    error_patterns = config.get("error_patterns", [])
    last_alert_time = 0
    alert_threshold = config.get("alert_threshold_minutes", 15) * 60 #convert to seconds.
    last_processed_positions = {}

    for log_file in log_files:
        if log_file not in last_processed_positions:
            last_processed_positions[log_file] = 0

    while True:
        for log_file in log_files:
            try:
                if not os.path.exists(log_file):
                    print(f"Warning: Log file '{log_file}' not found.")
                    continue

                with open(log_file, 'r') as f:
                    f.seek(last_processed_positions[log_file])
                    new_lines = f.readlines()
                    last_processed_positions[log_file] = f.tell()

                for line in new_lines:
                    for pattern in error_patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            current_time = time.time()
                            if current_time - last_alert_time >= alert_threshold:
                                send_alert(config, f"Error found in '{log_file}':\n{line}")
                                last_alert_time = current_time
                            else:
                                print(f"Error found, but within alert threshold. Skipping alert.")
                            break #no need to check other patterns if one matches.
            except Exception as e:
                print(f"Error monitoring '{log_file}': {e}")

        time.sleep(10) #checks every 10 seconds.

def main():
    config = load_config()
    if config:
        monitor_logs(config)

if __name__ == "__main__":
    main()
