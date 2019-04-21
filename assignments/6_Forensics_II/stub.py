#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic = struct.unpack("<L", data[0:4])[0]
version = struct.unpack("<L", data[4:8])[0]
timestamp = struct.unpack("<L", data[8:12])[0]
author = struct.unpack("<8s", data[12:20])
section_count = struct.unpack("<L", data[20:24])[0]
section1_type = struct.unpack("<L", data[24:28])[0]
section1_length = struct.unpack("<L", data[28:32])[0]
section1_value = struct.unpack("<24s", data[32:56])
section2_type = struct.unpack("<L", data[56:60])[0]
section2_length = struct.unpack("<L", data[60:64])[0]
section2_lat = struct.unpack("<d", data[64:72])[0]
section2_long = struct.unpack("<d", data[72:80])[0]
section3_type = struct.unpack("<L", data[80:84])[0]
section3_length = struct.unpack("<L", data[84:88])[0]
section3_value = data[88:202864]
section4_type = struct.unpack("<L", data[202864:202868])[0]
section4_length = struct.unpack("<L", data[202868:202872])[0]
section4_value = struct.unpack("<44s", data[202872:202916])
section5_type = struct.unpack("<L", data[202916:202920])[0]
section5_length = struct.unpack("<L", data[202920:202924])[0]
section5_value = struct.unpack("<80s", data[202924:203004])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % author)
print("SECTION_COUNT %d" % int(section_count))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
print("Section 1 type %d" % int(section1_type))
print("Section 1 length %d" % int(section1_length))
print("Section 1 value: %s" % section1_value)
print("Section 2 type %d" % int(section2_type))
print("Section 2 length %d" % int(section2_length))
print("Section 2 latitude: %s" % int(section2_lat))
print("Section 2 longitude: %s" % int(section2_long))
print("Section 3 type %d" % int(section3_type))
print("Section 3 length %d" % int(section3_length))
print("Section 4 type %d" % int(section4_type))
print("Section 4 length %d" % int(section4_length))
print("Section 4 value: %s" % section4_value)
print("Section 5 type %d" % int(section5_type))
print("Section 5 length %d" % int(section5_length))
print("Section 5 value: %s" % section5_value)
