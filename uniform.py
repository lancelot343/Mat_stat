import numpy as np
import random
import math
import collections
from scipy import stats
import copy

def intervals_zi_mi(array, interval, amount,l_lim):
     zi_min = min(array)
     zi_max = zi_min + interval
     counter = 0
     intervals = [zi_min]
     zi = []
     mi = []
     for i in range(amount):
        if array[i] <= round(zi_max,3)+0.003:
            counter += 1
            if i == amount - 1:
                intervals.append(zi_max)
                zi.append((zi_min + zi_max) / 2)
                mi.append(counter)
        else:
            intervals.append(zi_max)
            zi.append((zi_min + zi_max) / 2)
            mi.append(counter)
            zi_min = zi_max
            zi_max += interval
            counter = 1 

     return {'intervals':intervals,'zi':zi,'mi':mi}

def avarage(zi,mi,amount):
    sum = 0
    for i in range(len(zi)):
        sum+=zi[i] * mi[i]
    return round(sum / amount,3)

def standart(zi,mi,avarage, intervals_amount,amount):
    deviation = 0
    for i in range(intervals_amount):
       deviation +=((zi[i] - avarage) ** 2) * mi[i]
    variance = deviation / (amount - 1)
    return round(math.sqrt(variance),3)

def merge(table):
    i = 0
    k = 1
    while i < len(table['n*pi']):
        if len(table['n*pi']) == 1: break
        if table['n*pi'][i] < 10 or table['mi'][i] < 5:
            if i == 0 or i != len(table['n*pi']) - 1 and table['n*pi'][i + 1] <= table['n*pi'][i - 1]:
                table['mi'][i + 1] += table['mi'][i]
                table['pi'][i + 1] += table['pi'][i]
                table['n*pi'][i + 1] = table['n*pi'][i] + table['n*pi'][i + 1]
                table['intervals'][i + 1] = table['intervals'][i]
                table['zi'][i + 1] = (table['intervals'][i] + table['intervals'][i + 2]) / 2
            else:
                table['mi'][i - 1] += table['mi'][i]
                table['pi'][i - 1] = table['pi'][i] + table['pi'][i - 2]
                table['n*pi'][i - 1] = table['n*pi'][i - 1] + table['n*pi'][i]
                #table['intervals'][i] = table['intervals'][i]
                table['zi'][i - 1] = (table['intervals'][i] + table['intervals'][i - 1]) / 2

            table['intervals'].pop(i)
            table['mi'].pop(i)
            table['zi'].pop(i)
            table['pi'].pop(i)
            table['n*pi'].pop(i)
            i = - 1
        i += 1

def info_func(amount,left,right,significance):
    info = {}
    info['significance'] = significance
    info['amount'] = amount
    info['l_lim'] = left
    info['r_lim'] = right


    info['original_array'] = []
    for i in range(info['amount']):
        info['original_array'].append(round(random.uniform(info['l_lim'],info['r_lim']),3))
    info['array'] = sorted(info['original_array'])
   # info['array'] = [0.016, 0.024, 0.03, 0.067, 0.068, 0.115, 0.142, 0.182, 0.193, 0.209, 0.251, 0.252, 0.276, 0.304, 0.312, 0.315, 0.316, 0.336, 0.347, 0.359, 0.378, 0.381, 0.402, 0.404, 0.42, 0.424, 0.437, 0.46, 0.479, 0.483, 0.49, 0.519, 0.551, 0.563, 0.646, 0.654, 0.671, 0.718, 0.728, 0.836, 0.841, 0.909, 0.963, 0.964, 0.991, 1.008, 1.025, 1.032, 1.041, 1.071, 1.075, 1.22, 1.222, 1.223, 1.225, 1.235, 1.258, 1.277, 1.315, 1.364, 1.368, 1.474, 1.587, 1.594, 1.61, 1.617, 1.654, 1.698, 1.712, 1.746, 1.756, 1.762, 1.776, 1.846, 1.904, 1.929, 1.961, 1.967, 1.995, 2.007, 2.012, 2.07, 2.087, 2.097, 2.121, 2.127, 2.146, 2.157, 2.232, 2.272, 2.353, 2.407, 2.417, 2.452, 2.502, 2.52, 2.586, 2.669, 2.684, 2.692, 2.696, 2.743, 2.762, 2.779, 2.783, 2.802, 2.817, 2.84, 2.841, 2.907, 2.969, 2.969, 3.097, 3.103, 3.121, 3.131, 3.164, 3.169, 3.18, 3.185, 3.213, 3.227, 3.245, 3.264, 3.266, 3.297, 3.298, 3.329, 3.331, 3.357, 3.365, 3.367, 3.39, 3.416, 3.474, 3.507, 3.511, 3.514, 3.515, 3.519, 3.53, 3.579, 3.582, 3.634, 3.682, 3.687, 3.704, 3.712, 3.72, 3.759, 3.795, 3.874, 3.914, 3.924, 3.947, 3.957, 3.982, 4.021, 4.022, 4.025, 4.071, 4.116, 4.121, 4.144, 4.156, 4.189, 4.253, 4.268, 4.271, 4.275, 4.355, 4.362, 4.363, 4.43, 4.443, 4.451, 4.452, 4.468, 4.497, 4.565, 4.582, 4.601, 4.615, 4.629, 4.649, 4.671, 4.703, 4.766, 4.773, 4.783, 4.793, 4.803, 4.804, 4.85, 4.861, 4.892, 4.897, 4.916, 4.986, 4.986]

    r = math.log(info['amount'], 2)
    if r == int(r):
        info['intervals_amount'] = r + 1
    else:
        info['intervals_amount'] = math.ceil(r)


    
    info['interval'] = round((info['array'][-1] - info['array'][0]) / info['intervals_amount'],3)
    info['table'] = intervals_zi_mi(info['array'],info['interval'],info['amount'],info['l_lim'])
    info['avarage'] = avarage(info['table']['zi'],info['table']['mi'], info['amount']) 
    info['standart'] = standart(info['table']['zi'],info['table']['mi'],
                                       info['avarage'], info['intervals_amount'],info['amount'])

    info['a'] = round(info['avarage'] - math.sqrt(3) * info['standart']-0.0005,5)
    info['b'] = round(info['avarage'] + math.sqrt(3) * info['standart']+0.0005,5)

    info['table']['zi']=[round(i,4) for i in info['table']['zi']]
    info['table']['intervals']=[round(i,4) for i in info['table']['intervals']]

    info['i-vals_old']=[]
    for i in range(1,len(info['table']['intervals'])):
         info['i-vals_old'].append('( {} ; {} ]'.format(info['table']['intervals'][i-1],info['table']['intervals'][i]))

    info['table']['intervals'][0]=info['a']
    info['table']['intervals'][-1]=info['b']

    info['table']['zi'][0]=round((info['table']['intervals'][1]+info['table']['intervals'][0])/2,4)
    info['table']['zi'][-1]=round((info['table']['intervals'][-1]+info['table']['intervals'][-2])/2,4)

    info['table']['pi'] = []
    info['table']['n*pi'] = []

    for i in range(1,info['intervals_amount'] + 1):
        pi = (info['table']['intervals'][i] - info['table']['intervals'][i - 1]) / (info['b'] - info['a'])
        info['table']['pi'].append(round(pi,4))
        info['table']['n*pi'].append(round(pi * info['amount'],4))



    print('interval', "\t", 'zi',"\t",'mi'," ",'pi'," ",'n*pi')
    for i in range(info['intervals_amount']):
       print(info['table']['intervals'][i],"-", info['table']['intervals'][i+1], "\t",info['table']['zi'][i]," ",info['table']['mi'][i]," ",info['table']['pi'][i]," ",
             info['table']['n*pi'][i])
 
    info['zi_copy']=copy.deepcopy(info['table']['zi'])
    info['mi_copy']=copy.deepcopy(info['table']['mi'])
    info['pi_copy']=copy.deepcopy(info['table']['pi'])
    info['n*pi_copy']=copy.deepcopy(info['table']['n*pi'])
   

    merge(info['table'])

    info['table']['pi']=[round(i,4) for i in info['table']['pi']]
    info['table']['n*pi']=[round(i,4) for i in info['table']['n*pi']]
    info['table']['intervals']=[round(i,4) for i in info['table']['intervals']]
    info['table']['zi']=[round(i,4) for i in info['table']['zi']]

    info['d.f.'] = len(info['table']['mi'])- 3

    info['i-vals_new']=[]
    for i in range(1,len(info['table']['intervals'])):
         info['i-vals_new'].append('( {} ; {} ]'.format(info['table']['intervals'][i-1],info['table']['intervals'][i]))

    print('after')
    for i in range(len(info['table']['n*pi'])):
       print(info['table']['intervals'][i],"-", info['table']['intervals'][i+1],"\t", info['table']['zi'][i]," ",info['table']['mi'][i]," ",info['table']['pi'][i]," ",
             info['table']['n*pi'][i])

    print(info['array'])

    info['x^2emp']=0
    for i, el in enumerate(info['table']['mi']):
        info['x^2emp'] += ((el-info['table']['n*pi'][i])**2)/info['table']['n*pi'][i]

    info['x^2emp']=round(info['x^2emp'],5)
    info['x^2kr']=round(stats.chi2.isf(info['significance'],info['d.f.']),5)
  
    for k,v in info.items():
        print(k,'\t',v)
    return info