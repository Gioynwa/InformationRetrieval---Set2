

import math

sumGama = 0
sumVB = 0
counter = 0
for i in range(1, 10**6):
	counter += 1
	print(counter, " / ", str(10**6))
	power = 100
	j = 2 ** power
	while(1):
		if(i // j == 1):
			gama = 2 * power + 1
			vb = ((power // 7) + 1) * 8
			sumGama += gama
			sumVB += vb
			break
		power -= 1
		j = 2 ** power

div = sumVB / sumGama
print(div)






