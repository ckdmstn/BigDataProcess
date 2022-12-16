import sys
import numpy as np
import operator
import os

def fileToMatrix(trainingDataDirName):
	file_list = os.listdir(trainingDataDirName)
	
	list = [0 for n in range(len(file_list))]
	labels = []
	cnt = 0
	for fileName in file_list:
		file = trainingDataDirName + "/" + fileName 
		listFileName = fileName.split('_')
		labels.append(int(listFileName[0]))
		f = open(file)
		subList = []
		for line in f.readlines():
			for char in line:
				if char != '\n':
					subList.append(int(char))
		list[cnt] = subList; cnt += 1
	
	retMat = np.array(list)

	return retMat, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]



trainingDataDirName = str(sys.argv[1])
testDataDirName = str(sys.argv[2])

dataSet, labels = fileToMatrix(trainingDataDirName)

file_list = os.listdir(testDataDirName)
total_count = len(file_list)

for i in range(1, 21):
	count = 0

	for fileList in file_list:
		fileName = testDataDirName + "/" + fileList
		listFileName = fileList.split('_')	
		answer = int(listFileName[0])
		list = []

		f = open(fileName)

		for line in f.readlines():
			for char in line:
				if char != '\n':
					list.append(int(char))	

		inX = np.array(list)

		check = classify0(inX, dataSet, labels, i)

		if answer != check:
			count += 1

	error = count / total_count * 100

	print(round(error))
