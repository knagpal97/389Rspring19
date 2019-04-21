# Writeup 7 - Binaries I

Name: Kush Nagpal
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Kush Nagpal

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
#include <stdio.h>

int main() {
	int a = 0xfeedface;
	int b = 0x1ceb00da;

	printf("a = %d", a);
	printf("b = %d", b);

	a ^= b;
	b ^= a;
	a ^= b;

	printf("a = %d", a);
	printf("b = %d", b);
	return 0;
}

### Part 2 (10 Pts)

The program allows a user to print out 2 integer variables.  It then swaps  the value of these variables without an additional temporary variable through the use of xor and reprints the variables.