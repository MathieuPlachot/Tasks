#!/usr/bin/env python3

import socket
import sys
import time

taskTitle = sys.argv[1]
b = taskTitle.encode('utf-8')


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b)