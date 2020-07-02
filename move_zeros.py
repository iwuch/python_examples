ilst = [0,1,0,3,12]
# def move_zeros(lst):
# 	length = len(lst)
# 	i = 0
# 	for j in range(length):
# 		if lst[i] == 0:
# 			lst.pop(i)
# 			lst.append(0)
# 		else:
# 			i += 1
# 	return lst
# print(move_zeros(ilst))
def move_zeros(lst):
	length = len(lst)
	pindex = 0
	for i in ilst:
		if i!=0:
			lst[pindex]=i
			pindex+=1
	return lst[:pindex]+ [0]*(length-pindex)
print(move_zeros(ilst))