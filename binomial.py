import numpy as np
import collections
import math
from scipy import stats
import copy

def merge(info):
    i = 0
    while i < len(info['n*pi']):
        if info['n*pi'][i] < 10 or info['mi'][i]<5:
            if i == 0 or (i != len(info['n*pi'])-1 and info['n*pi'][i+1] < info['n*pi'][i-1]):
                info['mi'][i+1] += info['mi'][i]
                info['pi'][i+1] += info['pi'][i]
                info['n*pi'][i+1] = info['n*pi'][i]+ info['n*pi'][i+1]

                if type(info['xi'][i+1]) is tuple and type(info['xi'][i]) is tuple:
                    info['xi'][i+1]=info['xi'][i]+info['xi'][i+1]
                elif type(info['xi'][i+1]) is tuple:
                    info['xi'][i+1]=(info['xi'][i],)+info['xi'][i+1]
                elif type(info['xi'][i]) is tuple:
                    info['xi'][i+1]=info['xi'][i]+(info['xi'][i+1],)
                else: info['xi'][i+1]= (info['xi'][i],info['xi'][i+1])

            else:
                info['mi'][i-1] += info['mi'][i]
                info['pi'][i-1] = info['pi'][i]+ info['pi'][i-1]
                info['n*pi'][i-1] = info['n*pi'][i-1]+info['n*pi'][i]

                if type(info['xi'][i-1]) is tuple and type(info['xi'][i]) is tuple:
                    info['xi'][i-1]=info['xi'][i-1]+info['xi'][i]
                elif type(info['xi'][i]) is tuple:
                    info['xi'][i-1]=(info['xi'][i-1],)+info['xi'][i]
                elif type(info['xi'][i-1]) is tuple:
                     info['xi'][i-1]+=(info['xi'][i],)
                else: info['xi'][i-1]= (info['xi'][i-1],info['xi'][i])

            info['mi'].pop(i)
            info['xi'].pop(i)
            info['pi'].pop(i)
            info['n*pi'].pop(i)
            i =- 1
        i += 1

def info_func(amount,left,N,significance=0.05):
    info = {}
    info['significance']=significance 
    info['amount'] = amount
    info['N'] = N
    info['left'] = left
    info['original_array'] = np.random.randint(info['left'], info['N']+1,info['amount'])
    info['array'] = sorted(info['original_array'])

    table = collections.OrderedDict(collections.Counter(info['array']))
    info['xi'] = list(table.keys())
    info['mi'] = list(table.values())
    table.clear()

    sum=0
    for i in range(len(info['xi'])):
        sum+=info['xi'][i] * info['mi'][i]

    info['p*'] = round(sum/(info['N']*info['amount']),4)
    info['q*'] = 1-info['p*']
  

    info['pi']=[]
    info['n*pi']=[]
    for i in range(info['N']+1):
        pi=math.comb(info['N'],i)*info['p*']**i*info['q*']**(info['N']-i)
        info['pi'].append(round(pi,4))
        info['n*pi'].append(round(pi*info['amount'],4))

    print('xi'," ",'mi'," ",'pi'," ",'n*pi')
    for i in range(info['N']+1):
       print(info['xi'][i]," ",info['mi'][i]," ",info['pi'][i]," ",info['n*pi'][i])

    info['xi_copy']=copy.deepcopy(info['xi'])
    info['mi_copy']=copy.deepcopy(info['mi'])
    info['pi_copy']=copy.deepcopy(info['pi'])
    info['n*pi_copy']=copy.deepcopy(info['n*pi'])

    merge(info)
   
    info['d.f.']=len(info['xi'])-2
    info['pi']=[round(i,4) for i in info['pi']]
    info['n*pi']=[round(i,4) for i in info['n*pi']]

    info['x^2emp']=0
    for i in range(len(info['n*pi'])):
         info['x^2emp']+=(info['mi'][i]-info['n*pi'][i])**2/info['n*pi'][i]
    info['x^2emp']=round(info['x^2emp'],5)
    for i in range(len(info['n*pi'])):
       print(info['xi'][i]," ",info['mi'][i]," ",info['pi'][i]," ",info['n*pi'][i])

    info['x^2kr']=round(stats.chi2.isf(info['significance'],info['d.f.']),5)
    print(info['x^2emp'])
    print(len(info['xi']))
    print(info['d.f.'])
    print(info['x^2kr'])
    return info
   