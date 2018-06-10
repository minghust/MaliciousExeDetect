# MaliciousExeDetect
Topic: **datamining**

dataset: [(UCI) Detect Malacious Executable(AntiVirus) Data Set](https://archive.ics.uci.edu/ml/datasets/Detect+Malacious+Executable%28AntiVirus%29)

## Step
#### read data

```python
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
```

## Reference
A hybrid Model to detect malacious executable( using data mining and machine learning concept) by -- MM Masud , Latifur Khan, Bhavani Thuraisingham

## LICENSE

```
MIT License

Copyright (c) 2018 Ming Zhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

