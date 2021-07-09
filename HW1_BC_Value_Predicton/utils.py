import pathlib
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

mypath = 'C:/Users/bbb50/Desktop/Python/hw1/exchange/train_bc_val'
file_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count = 6675
for i in file_list:
    old = mypath + '/' + i + '.npy'
    new = mypath + '/sort_' + str(count) + '.npy'
    os.rename(old, new)
    count = count + 1


class readFile():
    def __init__(self, file):
        # if file == 'y':

        # else:

        self.bc_value, s_list, t_list, self.deg_list, n = [], [], [], [], 0
        for line in urllib.request.urlopen(url2):
            _, v = line.decode('utf-8').split()
            self.bc_value.append([n, math.log(float(v)+1e-8)])
            n += 1
        for x in range(len(self.bc_value)):
            self.deg_list.append([0, 1, 1])
        for line in urllib.request.urlopen(url1):
            s, t = line.decode('utf-8').split()
            s, t = int(s), int(t)
            s_list.append(s)
            t_list.append(t)
            self.deg_list[s][0] += 1
            self.deg_list[t][0] += 1
        self.edge_index = [s_list+t_list, t_list+s_list]

    def get_deg_list(self):
        # print(self.deg_list)
        return torch.Tensor(self.deg_list).cuda()

    def get_edge_index(self):
        # print(self.edge_index)
        return torch.tensor(self.edge_index, dtype=torch.long).cuda()

    def get_bc_value(self):
        # print(self.bc_value)
        return self.bc_value


def takeSecond(elem):
    return elem[1]


def topN_accuracy(file, outs, n):
    predict_value, bc_value = [], []
    for i, j in enumerate(outs.tolist()):
        predict_value.append([i, *j])
    bc_value = f.get_bc_value()
    bc_value.sort(key=takeSecond, reverse=True)
    predict_value.sort(key=takeSecond, reverse=True)
    p, t = [], []
    for x in range(int(len(predict_value)*n/100)):
        p.append(predict_value[x][0])
        t.append(bc_value[x][0])
    # print(t)
    # print(p)
    return(len(set(t) & set(p)) / len(p))
