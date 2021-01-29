# This is a sample Python script.
import numpy as np
import pandas as pd
import datetime
from datetime import datetime

import matplotlib.pyplot as plt

df = pd.read_csv("MyDataFile.csv")


states = ["important","normal","not_important",'redundant']



list = df['prediction'].tolist()
print(list)
print('important ', list.count('important'))
print('not important ', list.count('not_important'))
plt.hist(list)
plt.show()
print('normal ' , list.count('normal'))
print('redundant ', list.count('redundant'))
init_state = np.array([list.count('important'),list.count('normal'), list.count('not_important'),list.count('redundant')])

transitions = [["II","IN","INT","IR"],["NI","NN","NNT","NR"],["NTI","NTN","NTNT","NTR"],["RI","RN","RNT","RR"]]
transitionMatrix = np.array([[0.7,0.1,0.1,0.1],[0.5,0.2,0.1,0.2],[0.1,0.2,0.6,0.1],[0.4,0.4,0.1,0.1]])#example . Compare different values

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 4:
    print("It does not work!")
else: print("Everything works")

a_val,b_val,c_val,d_val = [],[],[],[]#change this
for x in range(5):
    a_val.append(init_state[0])
    b_val.append(init_state[1])
    c_val.append(init_state[2])
    d_val.append(init_state[3])
    b = init_state
    init_state = transitionMatrix.dot(b)
# plotting
plt.figure(figsize=(11,8))
plt.plot( [x for x in range(5)], a_val, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4,label='Important')
plt.plot( [x for x in range(5)], b_val, marker='o', markerfacecolor='red', markersize=12, color='pink', linewidth=4,label='normal')
plt.plot( [x for x in range(5)], c_val, marker='o', markerfacecolor='orange', markersize=12, color='yellow', linewidth=4,label='not_important')
plt.plot( [x for x in range(5)], d_val, marker='o', markerfacecolor='yellow', markersize=12, color='red', linewidth=4,label='redundant')

plt.legend(loc='best')
plt.xlabel('Months')
plt.ylabel('Number of pictures')
plt.show()