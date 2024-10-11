#Simple Python Port Scanner

This is a basic port scanner scans for open ports in spesific range on target host.
It's a useful tool for learning basic network scanning and socket programming.

#Features
- Scans port from spesific range.
- Detects and displays open ports
- Uses Python's socket library

#Prerequisites
- Any version of Python 3 must be installed

#How to run
- python3 scanner.py <target_ip>

#Example
- python3 scanner.py 192.168.1.1

#Testing the scanner
- To test that program netcat should be installed
- Open a port
- Run the program

#How to install netcat
- sudo apt-get install netcat

#Opening port using netcat
- nc -lvp 80

#Running program
- python3 scanner.py 127.0.0.1

#Error handling
- Program handles errors such invalid IPs, unreachable hosts and interrupted execution.
