Name: Kush Nagpal
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Kush Nagpal

## Assignment Writeup

### Part 1 (40 pts)

Assuming that I have Elizabeth Moffet's phone number, I would use a carrier lookup website to determine the carrier of the phone.  After doing this, I will attempt to login to the user's cell phone account.  Since I will not know the password and I do not want to lock the account by attempting to fill in random passwords, I would press forgot password? and enter in the user's cell phone number to reveal the security questions.  I am assuming that the 3 security questions used for accessing the account will be 1. What's her mother maiden name?  2. What city was she born in? and 3. What was the name of her first pet?  This is a reasonable assumption to make because these are very common security questions.  I would call the cell provider spoofing Moffet's number and mention that I am unable to access her account and I don't remember the security questions.  I will mention that I urgently need to access the account in order to pay my cell phone bill for the month.  I will use the same crying baby video as shown in the video we watched in class and mention as a result, I can't call back at a later time.  I would make sure to act confidently and behave in the same way I would if I was locked out of my own account.  If I can fool the representative into providing me with the answers to the security questions, I can change the answers to something arbitrary, change the password to something arbitrary, and dismiss the call.  If this does not work, I will look to find other providers where her phone number or email are used and try the same approach.  To answer the question about Moffet's pin number I would send a phishing sms to Moffet stating that her bank card needs to be replaced and ask her to enter her pin code on a fake website.  To figure out the browser that she uses most frequently I would call her and act as the cloud computing website (DigitalOcean) that runs 1337bank.money and mention that I haven't been retrieving data over some time.  While trying to troubleshoot the issue, I will instruct Moffet to go to a vulnerable website which may reveal this information.



### Part 2 (60 pts)

1. Use strong passwords.  The password used to sign in to the client server was only 10 characters long, consisting of solely lowercase letters.  This password is of low complexity and could easily be hacked in a day according to https://blog.preempt.com/weak-passwords.  Make sure you are not reusing passwords.  Since one of your passwords has been revealed, I should not be able to use it to sign into another website with the same username.
2. Make sure that there are no open ports.  Open ports are a major vulnerability and can be exploited through buffer overflow attacks or other vulnerabilities.  One open port allowed me to connect to your system shell.  To close open ports, log into DigitalOcean, go to your control panel, click on droplets, then click on networking, and then click on firewalls.  You can close unused ports here.
3. Don't use the same work email, username, and passwords for your personal accounts.  Since your web server has been compromised, I can use the information I retrieved to hack into any accounts using your email or username if you were not careful with your password.  If you change your email or username, your accounts will be safe even if your web server gets attacked again hypothetically.