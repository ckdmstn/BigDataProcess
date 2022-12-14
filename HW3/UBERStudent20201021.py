#!/usr/bin/python3
import sys
import calendar

filename = str(sys.argv[1])
outputFilename = str(sys.argv[2])

dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
strList = []
with open(filename, "rt") as fp:
	for line in fp:
		list = line.split(",")
		date = list[1].split("/")

		year = int(date[2])
		month = int(date[0])
		day = int(date[1])
		dayOfW = calendar.weekday(year, month, day)
		list3 = list[3][0:-1]
		uList = [list[0], dayofweek[dayOfW], int(list[2]), int(list3)]

		index = len(strList)
		for i, s in enumerate(reversed(strList)):
			if s[0] == list[0]:
				index = index-i
				break;
		strList.append(uList)
		i = len(strList)-2
		while i >= index:
			strList[i+1] = strList[i]
			i -= 1
		strList[index] = uList 

uberList = []
for li in strList:
	isExist = False
	for ul in uberList:
		if ul[0] == li[0] and ul[1] == li[1]:
			ul[2] += li[2]
			ul[3] += li[3]
			isExist = True
	if isExist == False:
		uberList.append(li)

with open(outputFilename, "wt") as fp:
	for i in range(len(uberList)):
		fp.write("%s,%s %d,%d\n" % (uberList[i][0], uberList[i][1], uberList[i][2], uberList[i][3]))
