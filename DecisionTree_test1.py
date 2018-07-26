#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/7/25 21:02
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  DecisionTree
# @File      :  DecisionTree_test1.py
# @Software  :  PyCharm Community Edition

# ********************************************************* 
from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob,2)
	return shannonEnt

def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels

def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if infoGain > bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature

if __name__ == '__main__':

	myDat,labels = createDataSet()
	shannonEnt1 = calcShannonEnt(myDat)
	print(shannonEnt1)
	myDat[0][-1] = 'maybe'
	shannonEnt2 = calcShannonEnt(myDat)
	print(shannonEnt2)

	print(myDat)
	splitResult1 = splitDataSet(myDat,0,1)
	print(splitResult1)
	splitResult2 = splitDataSet(myDat,0,0)
	print(splitResult2)

	bestFeature = chooseBestFeatureToSplit(myDat)
	print(bestFeature)
