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
