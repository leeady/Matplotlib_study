import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./data/day.csv')
col = ['temp','atemp']
data=data[col]

fig,ax = plt.subplots() #plt.subplots() 返回一个 Figure实例fig 和一个 AxesSubplot实例ax
ax.scatter(data['temp'],data['atemp'])
ax.set_xlabel('temp')
ax.set_ylabel('atemp')

# plt.savefig('./data/散点图.png',dpi=120)
plt.show()
plt.close()

