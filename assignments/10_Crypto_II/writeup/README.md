# Crypto II Writeup

Name: Kush Nagpal
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Kush Nagpal

## Assignment Writeup

### Part 1 (70 Pts)

Opening the gpg file outputs the following message:

hello! if you're reading this, then you've successfully decrypted this message
your flag is: CMSC389R-{m3ss@g3_!n_A_b0ttl3}
mention this flag in your part 1 writeup!
your directions:
type `gpg --list-secret-keys` and take a screenshot to verify that this
`key.asc` file has been properly imported.
next, create a text file called `signature.txt` and write the following inside:
"My name is <your name here>!"
replacing the <your name here> part with your actual name.
Once you've created this file, use `gpg` to sign the file with this new imported
keyand output it as `signature.txt.asc`. make sure to use the `--clearsign`
flag to produce an ASCII-armored output.
Upload only the `signature.txt.asc` file, and make sure it is named as such,
otherwise the grading script will NOT find it and properly, and you will not
receive credit for this part.

gpg --list-secret-keys
/home/knagpal/.gnupg/secring.gpg
--------------------------------
sec   4096R/C7D32E64 2019-04-26
uid                  CMSC389R <fake@email.com>
ssb   4096R/2A00E69B 2019-04-26

Uploaded signature.txt.asc.

### Part 2 (30 Pts)

The picture after encrypting using CBC is completely randomized.  The coloring of pixels of completely randomized and it is difficult to learn anything about the image.
The picture after encrypting using ECB is not randomized.  The white background has been converted to gray pixels, the red oval has been converted to a blue oval, and the teal rectangle has been converted to a light green oval.
CBC is a more secure encryption algorithm.  After ECB encryption, the picture still retains the oval and rectangle present in the original image.  This happens because in ECB encryption, the plaintext input into the block cipher is not randomized by xoring the plaintext with either the iv or previous ciphertext.  As a result, this leaves information about the plaintext.  However, after CBC encryption, there is no information present about the image, which makes it more secure.  By xoring the first block of plaintext with the iv and subsequent plaintext blocks with the previous ciphertext, no information is leaked about the plaintext.
