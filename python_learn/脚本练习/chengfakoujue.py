#! /usr/bin/python3
for i in range(1,10):
	for j in range(1,i+1):
		if i<=j:
			print("%d*%d=%d"%(i,j,i*j),end="	")
		else:
			print("%d*%d=%d"%(j,i,j*i),end="	")
	print()
