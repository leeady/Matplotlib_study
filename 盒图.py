import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./data/day.csv')

fig,ax = plt.subplots()
data_columns=['temp','atemp']
ax.boxplot(data[data_columns].values)

ax.set_xticklabels(data_columns,rotation=45)#设置x轴标签
ax.set_xlabel('type')#设置x轴标题

ax.set_ylim(0,2)#设置y轴上下限

# plt.savefig('./data/盒图.png',dpi=120)
plt.show()