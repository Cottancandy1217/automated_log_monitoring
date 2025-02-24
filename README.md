# Automated Server Log Monitoring and Alerting

## Project Overview

This project implements an automated system for monitoring server log files for specific error patterns and sending alerts. It uses Python to continuously scan log files, regular expressions to identify error patterns, and email to send alerts. This system is designed to provide proactive monitoring of server health and assist in rapid incident response.

## Features

* **Continuous Log Monitoring:** The system continuously monitors specified log files for new entries.
* **Regular Expression Pattern Matching:** Uses regular expressions to detect complex error patterns within log entries.
* **Configurable Error Patterns:** Error patterns can be easily configured in a JSON configuration file.
* **Email Alerts:** Sends email alerts when a matching error pattern is detected.
* **Configurable Alert Recipients:** Alert recipients can be configured in the JSON configuration file.
* **Avoids Alert Storms:** Implements time based thresholds to prevent too many emails from being sent in a short amount of time.

## Usage

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd automated-log-monitoring
    ```

2.  **Configure `config.json`:**

    * Open `config.json` in a text editor.
    * Modify the `log_files` array to include the paths to the log files you want to monitor.
    * Modify the `error_patterns` array to include the regular expressions for the error patterns you want to detect.
    * Modify the `alert_recipients` array to include the email addresses of the alert recipients.
    * Modify the `smtp_server`, `smtp_port`, `smtp_user`, and `smtp_password` fields to configure your SMTP server settings.
    * Modify the `alert_threshold_minutes` field to set the time between emails, preventing alert storms.

    Example `config.json`:

    ```json
    {
      "log_files": ["/var/log/syslog", "/var/log/application.log"],
      "error_patterns": ["error", "failed", "critical", "Exception"],
      "alert_recipients": ["[email address removed]", "[email address removed]"],
      "smtp_server": "[smtp.example.com](https://www.google.com/search?q=smtp.example.com)",
      "smtp_port": 587,
      "smtp_user": "your_smtp_user",
      "smtp_password": "your_smtp_password",
      "alert_threshold_minutes": 15
    }
    ```

3.  **Run `log_monitor.py`:**

    ```bash
    python3 log_monitor.py
    ```

    * The script will continuously monitor the specified log files and send alerts when error patterns are detected.

## Dependencies

* Python 3
* Standard Python libraries (smtplib, re, json, os, time)

## Author
* Angelee Morquin

## Contact

Email: sweety.angel1217@gmail.com
LinkedIn: https://www.linkedin.com/in/angelee-morquin-934b51125/
