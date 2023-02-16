#!/usr/bin/env python3
"""
a script that reads <stdin> line by line and computes metrics
"""
import sys
import signal


total_file_size = 0
lines_by_status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


# Define signal handler for CTRL + C
def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)

# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Function to parse the log line and update the metrics
def parse_log_line(line):
    global total_file_size
    global lines_by_status_code
    global line_count

    # Parse log line
    try:
        ip, date, request, status_code, file_size = line.split(" ")
        if request != "GET /projects/260 HTTP/1.1":
            return
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        return

    # Update metrics
    total_file_size += file_size
    lines_by_status_code[status_code] += 1
    line_count += 1

    # Print stats if we've processed 10 lines
    if line_count % 10 == 0:
        print_stats()

# Function to print the current statistics
def print_stats():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(lines_by_status_code.keys()):
        if lines_by_status_code[status_code] > 0:
            print(f"{status_code}: {lines_by_status_code[status_code]}")

# Read input from stdin line by line
for line in sys.stdin:
    parse_log_line(line)

    # Print stats if we've processed 10 lines
    if line_count % 10 == 0:
        print_stats()
