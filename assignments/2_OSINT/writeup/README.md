# Writeup 2 - OSINT

Name: *Kush Nagpal*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Kush Nagpal*

## Assignment Writeup

### Part 1 (45 pts)

I was given the user_id v0idcache.  Given this, I went to usersearch.org and found that the user has accounts with twitter, videobam, and reddit.
The user also had a strange conversation with a user named fl1nch as found on pastebin.  I was unable to find more information about fl1nch.
On v0idcache's twitter account, I was able to view the individual's name: Elizabeth Moffet and website: http://1337bank.money/.
The website reveals that she works for elite bank for the 1337 Haxor.  Her email address is also listed on the website: v0idcache@protonmail.com.  The email was not pwned.
The user's reddit account lists a post with the following flag: CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}
I added /robots.txt to discover a secret directory called /secret_directory.  This returned the following flag:
Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}
I realized that the website is a hidden git repo.  Accessing http://1337bank.money/.git/logs/refs/heads/master gave me the following flag:
revealed flag: CMSC389R-{h1d3_s3cret_g1ts}
Using cubdomain, I inputted the website and discovered that the IP address is 142.93.136.81.  The DigitalOcean server is based in Amsterdam.
With the ip address in hand, I proceeded to use nmap -p- to look for open ports.  The following ports are open:
22 ssh
25 smtp
80 http
110 pop3
119 nntp
143 imap
465 smtps
554 rtsp
563 snews
587 submission
993 imaps
995 pop3s
7070 realserver
When inputting the ip address in Censys, it revealed the server runs in Ubuntu.
Inputting the ip address in dnsdumpster returns the following flag: "CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}"

### Part 2 (75 pts)
I was able to determine that the open port is 1337.  The username of the shell service is v0idcache, as expected.  I iterated through each password in rockyou.txt and discovered that the password is linkinpark.
Once I got access to the shell, I checked the contents of each folder.  I found the file flag.txt in the home directory, which revealed the flag: Good work!  Here's a flag: CMSC389R-{brut3_f0rce_m4ster}

