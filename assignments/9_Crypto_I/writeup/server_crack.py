#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    f = open("hashes.txt",'r') # open and read hashes.txt
    hashes = f.read().split("\n")
    f = open("passwords.txt",'r')
    passwords = f.read().split("\r\n") # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    for i in range(3):
        data = s.recv(1024).split("\n")
        for c in characters:
            for p in passwords:
                inp = c + p
                hashed = hashlib.sha256(inp).hexdigest()
                if hashed == data[2]:
                    s.send(c+p+"\n")

    data = s.recv(1024).split("\n")
    print(data[0])
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
