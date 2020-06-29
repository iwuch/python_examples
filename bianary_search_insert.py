import random
N = 100
k = 10
target =25
slst = sorted([int(random.random()*N) for _ in range(k)])

def binary_search_insert(slst,target):
	length = len(slst)
	right = length-1
	left = 0
	while(right >= left):
		mid = (right+left)//2
		if target > slst[mid]:
			left = mid+1
		if target < slst[mid]:
			right = mid -1
		if target == slst[mid]:
			return mid
	return left
print(slst)
print(target)
print(binary_search_insert(slst,target))