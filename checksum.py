def calc_checksum(s):
	sum = 0
	for i in range(len(s)):
		sum = sum + ord(s[i])
	temp = sum % 256
	rem = -temp
	return '%2X' % (rem & 0xFF)
a=input("Entrez mot: ")
print(calc_checksum(a))
