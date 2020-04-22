##############################################

import math

def encoderZk(number, k):

	# finding interval of number 5
	h = 0
	while(1):
		start = 2 ** (h * k)
		end = 2 ** ((h + 1) * k) - 1
		if(number >= start and number <= end):
			break
		else:
			h += 1

	print("Number =", number, "with k =", k, "in z code:")

	# finding unary code of (h + 1)
	unary = [0] * (h + 1)
	for i in range(h + 1):
		if(i != h):
			unary[i] = 0
		else:
			unary[i] = 1

	startMinimal = 0
	endMinimal = 2 ** ((h + 1) * k) - 2 ** (h * k) - 1
	numberForMinimal = number - 2 ** (h * k)


	# exception when number is 2 ** (h * k)
	if(number == 2 ** (h * k)):
		for j in range(h + 1):
			print(unary[j], end =" ")
		for j in range(h + 1, (h + 1) * (k + 1) - 1):
			print(0, end=" ")
		print()
		return

	# encoding numberForMinimal into minimal binary code
	# our x = numberForMinimal
	# our interval is [0, z - 1] = [startMinimal, endMinimal]
	# our s = log(z)
	# print(unary)

	z = endMinimal + 1
	s = int(math.log2(z)) + 1

	for j in range(h + 1):
		print(unary[j], end =" ")

	if(numberForMinimal < (2 ** s - z)):
		binary = "{0:0b}".format(numberForMinimal)
		if(len(binary) != s - 1):
			for m in range(s - 1 - len(binary)):
				print(0, end=" ")
		print(binary)
	else:
		numberForMinimal = numberForMinimal - z + 2 ** s
		binary = "{0:0b}".format(numberForMinimal)
		if(len(binary) != s):
			for m in range(s - len(binary)):
				print(0, end=" ")
		print(binary)


for i in range(1, 16):
	encoderZk(i, 1)

for i in range(1, 16):
	encoderZk(i, 2)

for i in range(1, 16):
	encoderZk(i, 3)

for i in range(1, 16):
	encoderZk(i, 4)

