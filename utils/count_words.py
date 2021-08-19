import sys
# import os

filename = str(sys.argv[1])

if str(sys.argv[2]) == "s":
	tc = " "
else:
	tc = ""

with open(filename,"r") as f:
	if tc == "":
		print(len(f.read()))
	else:
		print(f.read().count(tc))