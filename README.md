# Network Configuration Auditor

## Overview

This project is a command-line tool built with Python to automatically audit a Cisco network device's configuration file for compliance with basic security policies. The script uses regular expressions (regex) to parse the configuration text and validate that critical security features are correctly implemented.

This tool was created to demonstrate skills in Python scripting, automation, text processing, and fundamental network security principles.

## Features

- **Security Compliance Checks:** Verifies key security settings, including:
  - Presence of a secure `enable secret` password.
  - Configuration of a warning banner (MOTD).
  - Absence of insecure clear-text passwords on the console line.
- **Clear Pass/Fail Reporting:** Provides simple and clear output for each compliance check.
- **File-Based:** Reads from a local `.txt` configuration file, making it easy to test and demonstrate without needing a live network device.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Clone this repository: `git clone <your_repository_link_here>`
3.  Navigate to the project directory: `cd <repository_name>`
4.  Run the script: `python audit.py`

The script will automatically audit the included `config.txt` file and print the results to the console.

## Technologies Used

- **Python 3**
- **`re` module (Regular Expressions)**
-
