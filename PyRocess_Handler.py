import sys
import subprocess
import logging
import os
from subprocess import CalledProcessError
from datetime import datetime
from html import escape
from Logger import setup_logging

def main(message):
    # Setup logging
    log_dir = "./Log/PyRocess_Handler_Logging"
    log_file_prefix = "PyRocess_Handler"
    setup_logging(log_dir, log_file_prefix)

    # Get process_name
    process_name = sys.argv[1]

    # Validate process name
    if not process_name:
        logging.error("Invalid process name")
        return

    # Sanitize message to prevent XSS
    sanitized_message = escape(message)

    # Log the incoming request
    logging.info(f"Process started: {process_name}.py, Message: {sanitized_message}")

    # Execute the appropriate script based on process name
    try:
        subprocess.run(['python', f'./PyRocesses/API-Triggerd/Enabled/{process_name}/{process_name}.py', sanitized_message], check=True)
        logging.info(f"Process completed successfully: {process_name}.py")
    except CalledProcessError as e:
        logging.error(f"Failed to execute {process_name}.py: {e}")
        return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: PyRocess_Handler.py [process_name] [message]")
    else:
        main(sys.argv[2])  # Message is the second argument