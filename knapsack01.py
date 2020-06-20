import numpy as np
a1 = [100, 70, 50, 10]
a2 = [10, 4, 6, 12]
w = 12
def knapsack01(values,weights,capacity):
	n_knapsack = len(values)
	maxvalue_table = np.zeros((n_knapsack+1, capacity+1))
	for i in range(1,n_knapsack+1):
		for j in range(1,capacity+1):
			if weights[i-1] <= j:
				option1 = maxvalue_table[i-1][j]
				option2 = maxvalue_table[i-1][j-weights[i-1]] + values[i-1]
				maxvalue_table[i][j] = max(option1,option2)
			else:
				maxvalue_table[i][j]  = maxvalue_table[i-1][j]
	return maxvalue_table
maxvalue_table = knapsack01(a1,a2,w)
maxvalue = maxvalue_table[-1][-1]
print(maxvalue_table,'\n',maxvalue)