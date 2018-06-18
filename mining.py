#! /usr/bin/python3
# author: Ming Zhang

import fileinput
from sklearn import svm
import numpy as np 
import matplotlib.pyplot as plt

def readTrainData(inputFile):
    datalist = []
    type_list=[]
    sample_attr = []
    for line in fileinput.input(inputFile):
        datalist.append(line.split())

    for exe in datalist:
        exe_attr = []
        for i in range(1, len(exe)):
            if exe[i] == '-1':
                break
            else:
                exe_attr.append(int(exe[i].split(':', 1)[0]))
        
        # 数据清洗，去除无属性值的exe信息
        if len(exe_attr)!=0:
            type_list.append(int(exe[0])) # add +1 or -1 to type list
            sample_attr.append(exe_attr)
    
    maxdim = 0
    for sample in sample_attr:
        if maxdim < sample[-1]:
            maxdim = sample[-1]
    # maxdim = maxdim + 1
    
    x = []
    # 数据维度不一致，无法使用svm，此处将数据维度调整一致
    for sample in sample_attr:
        attr = [0]*maxdim
        for i in sample:
            attr[i-1] = 1
        x.append(attr)
    
    # 372 samples, each sample has 531 attributes
    return x, type_list, maxdim


def readTestData(inputFile, maxdim):
    datalist = []
    type_list=[]
    sample_attr = []
    for line in fileinput.input(inputFile):
        datalist.append(line.split())

    for exe in datalist:
        exe_attr = []
        for i in range(1, len(exe)):
            if exe[i] == '-1':
                break
            else:
                exe_attr.append(int(exe[i].split(':', 1)[0]))
        
        # 数据清洗，去除无属性值的exe信息
        if len(exe_attr)!=0:
            type_list.append(int(exe[0])) # add +1 or -1 to type list
            sample_attr.append(exe_attr)
    
    x = []
    # 将数据维度调整与训练集一致
    for sample in sample_attr:
        attr = [0]*maxdim
        for i in sample:
            attr[i-1] = 1
        x.append(attr)
    return x, type_list

#### read train data
x, y, maxdim = readTrainData("dataset.train")

#### start to train out classifier
classifier = svm.SVC(kernel='poly', gamma=0.1)
classifier.fit(x, y)

# classifier_2 = svm.SVC(kernel='sigmoid')
# classifier_2.fit(x, y)

# classifier_3 = svm.SVC(kernel='sigmoid')
# classifier_3.fit(x, y)

# classifier_4 = svm.SVC(kernel='sigmoid')
# classifier_5.fit(x, y)
#### read test data
x, y = readTestData("test.txt", maxdim)

predict = []

######################## Test ##########################
rightNum = 0
for i in range(0, len(y)):
    each_test = x[i]
    res=classifier.predict(np.array(each_test).reshape(1, -1))
    if y[i] == res.tolist()[0]:
        rightNum += 1

print("正确率："+str(rightNum/len(y)))