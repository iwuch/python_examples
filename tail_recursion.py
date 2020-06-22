import random
##普通递归：最后一个指令是加法指令
##在最后一次递归调用之后还有一个额外的计算
def sumr(lst):
	if len(lst)==0:
		return 0
	else:
		return lst[-1]+sumr(lst[:-1])

##尾递归：递归调用是函数的最后一条语句
def sumt(lst,acc):
	def helper(lst,acc):
		if len(lst) == 0:
			return acc
		else:
			return helper(lst[1:],acc+lst[0])
	return helper(lst[1:],lst[0]+acc)

rlst = random.sample(range(1,10),5)
print(rlst)
print(sumt(rlst,0))