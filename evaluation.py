from tqdm import tqdm
import os
import yaml
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import prettytable as pt

listTime,listHlnode,listLlnode={},{},{}
for agentNum in range(5,22):
    try:
        sumTime,sumHlnode,sumLlnode=[],[],[]
        fileNum=0
        outputPath='mission/output/'+str(agentNum)+'/'
        fileList=os.listdir(outputPath)
        print('\nagents num:%d is processing'%agentNum)
        for sampleIndex in range(len(fileList)):
            sample=fileList[sampleIndex]
            fileNum+=0
            argsOutput = outputPath+sample
            with open(argsOutput,  'r') as param_file:
                try:
                    param = yaml.load(param_file, Loader=yaml.FullLoader)
                except yaml.YAMLError as exc:
                    print(exc)
            hlnode = param["hlNode"]
            llnode = param["llNode"]
            timer=param['time']
            sumTime.append(timer)
            sumLlnode.append(llnode)
            sumHlnode.append(hlnode)
        if fileNum==0:
            fileNum=1
        listTime[agentNum],listHlnode[agentNum],listLlnode[agentNum]=\
        sumTime,sumLlnode,sumHlnode
    except:
        print(outputPath)



succ=[]
for agentNum in range(5,22):
    outputPath='mission/output/'+str(agentNum)
    outputFile=os.listdir(outputPath)
    succRate=len(outputFile)/100
    succ.append(len(outputFile))
plt.figure()
plt.plot(list(range(5,22)),succ)
plt.title('Success rate. number of agents 8 × 8grid')
plt.xlabel('k`')
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(10))
plt.ylabel('Success rate')
plt.ylim()
plt.savefig('succ.png')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def list_generator(mean, dis, number):
    return np.random.normal(mean, dis * dis, number)

data = []
rang=range(5,22)
for agentNum in rang:
    d=listTime.get(agentNum)
    data.append(d)
ax.boxplot(data)
ax.set_xticklabels(list(rang))
plt.xlabel('k`')
plt.ylabel('time')
plt.savefig('runningtime.png')
plt.show()

def mean(l):
    f=sum(l)/len(l)
    return "%3.2f"%f
# tb = pt.PrettyTable( ["City name", "Area", "Population", "Annual Rainfall"])
tb = pt.PrettyTable()
tb.field_names = ["k" , "成功率" , "运行时间" , "低层节点数" , "高层节点数"]
for agentNum in range(5,22):
    itemList=[agentNum,len(listTime[agentNum]),mean(listTime[agentNum]),mean(listHlnode[agentNum]),
          mean(listLlnode[agentNum])]
    tb.add_row(itemList)
print(tb)

