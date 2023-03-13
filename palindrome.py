def isPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

s = "malayalam"
str1 = isPalindrome(s)

if (str1):
	print("The given word is Palindrome")
else:
	print("The given word is not a Palindrome")
