# Writeup 6 - Forensics

Name: Kush Nagpal
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Kush Nagpal

## Assignment Writeup

### Part 1 (45 Pts)

1. The ip address being attacked is 142.93.136.81.
2. The attacker used nmap and ftp.
3. The attacker has an ip address of 159.203.113.181.  The remaining ip addresses on the network capture are noise.
4. The attacker is stealing data on port 21.
5. The attacker is stealing a jpeg file called find_me.jpeg.
	a. The file type is JPEG.
	b. The picture was taken at 34 degrees south, 54 degrees west.  The attraction at this location is Los Dedos, Maldonado Department, Uruguay.
	c. The picture was taken at 2018:12:23 17:16:24.
	d. The camera that took this photo is an iPhone 8 back camera 3.99mm f/1.8.
	e. The photo was taken 4.5 m below sea level.
6. The attackers left greetz.fpff on the server.
7. This attack could be prevented by blocking all users who nmap 142.93.136.81.

### Part 2 (55 Pts)
1. greetz.fpff was generated at 1553660105, or Wednesday, March 27, 2019 12:15:05 AM.
2. greetz.fpff was authored by fl1nch.
3. Section 1:
	Type: ASCII
	Data: Hey you, keep looking :)
   Section 2:
	Type: Coordinate Pair
	Data: 52 deg north, 4 deg east (Amsterdam)
   Section 3:
	Type: PNG
	Data: Omitted
   Section 4:
	Type: ASCII
	Data: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSM (it is printed in reverse)
   Section 5:
	Type: ASCII
	Data: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

Flag: CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}

