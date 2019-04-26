#!/usr/bin/env python3

import hashlib
import string

def crack():
    f = open("hashes.txt",'r') # open and read hashes.txt
    hashes = f.read().split("\n")
    f = open("passwords.txt",'r')
    passwords = f.read().split("\r\n") # open and read passwords.txt
    characters = string.ascii_lowercase
    for c in characters:
        for p in passwords:
    		inp = c + p
    		hashed = hashlib.sha256(inp).hexdigest()
    		if hashed in hashes:
    			print(c + "+" + p+ ":" + hashed)
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()