#快捷键：Ctl+Y 删除一行
#快捷键：Ctl+D 复制一行
import matplotlib.pyplot as plt
import random as r
for i in range(1000):
	x = r.uniform(-10,10)
	y = r.uniform(-10,10)
	z1 = 5*x + y + 10
	z2 = x - y + 15
	z3 = 3*x - 5*y + 10
	if z1 > z2 and z1 > z3:
		plt.scatter(x, y, color = 'r')
	if z2 > z1 and z2 > z3:
		plt.scatter(x, y, color = 'k')
	if z3 > z1 and z3 > z2:
		plt.scatter(x, y, color = 'b')
plt.show()

# from matplotlib import pyplot as plot  # 用来绘制图形
# import numpy as np  # 用来处理数据
# from mpl_toolkits.mplot3d import Axes3D  # 用来给出三维坐标系。
# figure = plot.figure()
# # 画出三维坐标系：
# axes = Axes3D(figure)
# X = np.arange(-10, 10, 0.25)
# Y = np.arange(-10, 10, 0.25)
# # 限定图形的样式是网格线的样式：
# X, Y = np.meshgrid(X, Y)
# Z1 = 3*X + Y + 8
# axes.plot_surface(X, Y, Z1, cmap='rainbow')
# Z2 = X - Y + 15
# axes.plot_surface(X, Y, Z2, cmap='rainbow')
# Z3 = 3*X - 5*Y + 10
# axes.plot_surface(X, Y, Z3, cmap='rainbow')
# # 图形可视化：
# plot.show()