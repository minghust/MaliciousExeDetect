#! /usr/bin/python3

import fileinput
 
datalist = []
malicious_exelist = []
benign_exelist = []

for line in fileinput.input("dataset.train"):
    datalist.append(line.split())


for exe in datalist:
    exe_attr = []
    exe_attr.append(exe[0])
    for i in range(1, len(exe)):
        if exe[i] == '-1':
            break
        else:
            s = exe[i]
            exe_attr.append(exe[i].split(':', 1)[0])
    if exe[0] == '+1':
        benign_exelist.append(exe_attr)
    elif exe[0] == '-1':
        malicious_exelist.append(exe_attr)

print(benign_exelist)
print(malicious_exelist)


