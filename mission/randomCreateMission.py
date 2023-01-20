import yaml,os
from random import randint
from tqdm import tqdm
def saveMap(data,path):
    with open(path, encoding='utf-8',mode='w') as f:
        try:
            yaml.dump(data=data,stream=f,allow_unicode=True)
        except Exception as e:
            print(e)

def randonData(agentNum):
    data={}
    data['agents']=[]
    startSet,goalSet=set(),set()
    for i in range(agentNum):
        start=[randint(0,7),randint(0,7)]
        while startSet.__contains__(start[0]+start[1]*0.1):
            start=[randint(0,7),randint(0,7)]
        startSet.add(start[0]+start[1]*0.1)

        goal=[randint(0,7),randint(0,7)]
        while goalSet.__contains__(goal[0]+goal[1]*0.1):
            goal=[randint(0,7),randint(0,7)]
        goalSet.add(goal[0]+goal[1]*0.1)
        data['agents'].append({'start': start, 'goal': goal, 'name': 'agent'+str(i)})
    data["map"]={'dimensions':[8,8],'obstacles':[]}
    return data

if __name__=="__main__":
    for agentNum in range(5,22):
        main_path='input/'+str(agentNum)+'/'
        if not os.path.exists(main_path):  # 如果路径不存在
            os.makedirs(main_path)
        for sample in tqdm(range(1,101)):
            d=randonData(agentNum)
            saveMap(d,main_path+'input'+str(sample)+'.yaml')