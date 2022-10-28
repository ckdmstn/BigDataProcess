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
		str = list[0] + "," + dayofweek[dayOfW] + " " + list[2] + "," + list3

		index = len(strList)
		for i, s in enumerate(reversed(strList)):
			if s.startswith(list[0]):
				index = index-i
				break;
		strList.append(str)
		i = len(strList)-2
		while i >= index:
			strList[i+1] = strList[i]
			i -= 1
		strList[index] = str

with open(outputFilename, "wt") as fp:
	for line in strList:
		fp.write(line+"\n")
