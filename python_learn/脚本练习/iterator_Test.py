#! /usr/bin/python3
import sys
list = [1,2,3,4,5]
it = iter(list)
'''
for i in it:
	print(i,end=",")
'''
while True:
	try:
		print(next(it),end=",")
	except StopIteration:
		sys.exit()
