#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/7/27 16:33
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  DecisionTree
# @File      :  DecisionTree_test2.py
# @Software  :  PyCharm

# ********************************************************* 
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',
	                        va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)

def createPlot():
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	createPlot.ax1 =plt.subplot(111,frameon=False)
	plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('叶节点',(0.8,0.1),(0.3,0.8),leafNode)
	plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	plt.show()

if __name__ == '__main__':
	createPlot()