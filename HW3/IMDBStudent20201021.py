import sys

filename = str(sys.argv[1])
outputFilename = str(sys.argv[2])

genreDict = {}

with open(filename, "rt") as fp:
	for line in fp:
		list = line.split("::")
		genre = list[2].split("|")
		for g in genre:
			str = ""
			if g.endswith("\n"):
				str = g[0:-1]
			else:
				str = g
			if str not in genreDict:
				genreDict[str] = 1
			else:
				genreDict[str] += 1

with open(outputFilename, "wt") as fp:
	for g, n in genreDict.items():
		fp.write("%s %d\n" % (g, n))
