import math

def decodeZk(binaryWord, k):

	# finding h
	for i in range(len(binaryWord)):
		if(binaryWord[i] == '1' and len(binaryWord) == 1):
			print("Decoded number of binary word =", binaryWord,"with k =", k,"is", 1)
			return
		if(binaryWord[i] == '1'):
			h = i
			break

	# decoding minimal binary code
	endMinimal = 2 ** ((h + 1) * k) - 2 ** (h * k) - 1
	z = endMinimal + 1
	s = int(math.log2(z)) + 1

	pre = "0b"
	minimalB = binaryWord[-(len(binaryWord) - (h + 1)):]
	toConvert = pre + minimalB

	checkNumber = int(toConvert, 2) + z - 2 ** s
	if(checkNumber < (2 ** s - z)):
		number = int(toConvert, 2) + 2 ** (h * k)
	else:
		number = int(toConvert, 2) + z - 2 ** s + 2 ** (h * k)
	
	print("Decoded number of binary word =", binaryWord,"with k =", k,"is", number)

decodeZk("1", 1)
decodeZk("010", 1)
decodeZk("011", 1)
decodeZk("00100", 1)
decodeZk("00101", 1)
decodeZk("00110", 1)
decodeZk("00111", 1)
decodeZk("0001000", 1)

decodeZk("10", 2)
decodeZk("110", 2)
decodeZk("111", 2)
decodeZk("01000", 2)
decodeZk("01001", 2)
decodeZk("01010", 2)
decodeZk("01011", 2)
decodeZk("011000", 2)

decodeZk("100", 3)
decodeZk("1010", 3)
decodeZk("1011", 3)
decodeZk("1100", 3)
decodeZk("1101", 3)
decodeZk("1110", 3)
decodeZk("1111", 3)
decodeZk("0100000", 3)

decodeZk("1000", 4)
decodeZk("10010", 4)
decodeZk("10011", 4)
decodeZk("10100", 4)
decodeZk("10101", 4)
decodeZk("10110", 4)
decodeZk("10111", 4)
decodeZk("11000", 4)

