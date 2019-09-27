
import numpy as np
import matplotlib.pyplot as plt
# from pylab import *
# plt.rcParams['font.sans-serif'] = ['SimHei'] #网上搜索可以设置中文编码的方法，但不成功
# plt.rcParams['axes.unicode_minus'] = False

# 定义数据部分
x = np.arange(0.0, 10, 0.2) #设置一个从0到10，每隔0.2取一个数的array
y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.sqrt(x)

# 绘制基本曲线(color为曲线颜色，linewidth为曲线宽度，linestyle为曲线样式（详见line_style.png），
# marker为曲线里面每一个数据点的样式（详见marks.png），label为该曲线的标签（声明之后在下面设置图例里面引用）)
plt.plot(x, y1, color='red', linewidth=1.5, linestyle='-', marker='.',label='cos(x)')
plt.plot(x, y2, color='blue', linewidth=1.5, linestyle='--', marker='.',label='sin(x)')
plt.plot(x, y3, color='green', linewidth=1.5, linestyle='-.', marker='.',label='sqrt(x)')

# 设置x，y轴的刻度取值范围
plt.xlim(-1, x.max() * 1.1)
plt.ylim(-1.5,4.0)
#设置x，y轴的刻度标签值
plt.xticks([0,2,4,6,8,10],['0',r'two',r'four',r'six',r'eight',r'ten'])
plt.yticks([-1,0,1,2,3,4,5],[r'-one',r'zero',r'one',r'two',r'three',r'four',r'five'])
#设置标题
plt.title('function of cos(),sin(),sqrt()',fontsize=19)#fontsize为标题大小
plt.xlabel('x')
plt.ylabel('y=f(x)')
#设置图例
plt.legend(loc='best')#前提是在plt.plot函数中指明了标签(label=)才可以使用
#设置网格线
plt.grid(True)#默认为无
#保存为图片
# plt.savefig('./data/image.png',dpi=120)#dpi为图片像素

#显示统计图
plt.show()


