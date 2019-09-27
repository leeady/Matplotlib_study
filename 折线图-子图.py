import matplotlib.pyplot as plt
import pandas as pd

#准备数据
data = pd.read_csv('./data/day.csv')
data = data[['dteday','temp']]  #提取文档中 日期（dteday）和温度（temp）两列
data = data[0:12]       #取前12个行数据
# print(data.head())

#开始作图
fig = plt.figure(figsize=(12,8))#创建figure对象,可以设置显示的图框的长宽
ax1 = fig.add_subplot(1,2,1)#添加子图，按一行两列显示，第三个参数为放置位置
ax2 = fig.add_subplot(1,2,2)

ax1.plot(data['dteday'],data['temp'],color = 'black',label='y=f(x)')
ax1.set_xticklabels(data['dteday'],rotation=45) #设置x轴的标签值，角度为45度
ax1.set_xlabel('day')
ax1.set_ylabel('temp')
ax1.set_title('About day and temp 1')
ax1.legend(loc='best')
ax1.grid(True)

ax2.plot(data['dteday'],data['temp'],color = 'black',label='y=f(x)')
# ax2.set_xlim(min(data['dteday'])*2,max(data['dteday'])*2) #日期不能使用max和min函数
ax2.set_ylim(min(data['temp'])-0.5,max(data['temp'])+0.5)
ax2.set_xticklabels(data['dteday'],rotation=45)
ax2.set_xlabel('day')
ax2.set_ylabel('temp')
ax2.set_title('About day and temp 2')
ax2.legend(loc='best')

# plt.savefig('./data/折线图_子图.png',dpi=120)
plt.show()
plt.close()
