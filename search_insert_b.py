import random
N = 100
k = 10
target = 25
# slst = sorted(random.sample(range(N),k))
# slst = sorted([int(random.random()*N) for _ in range(k)])
def search_insert(nums,target):
	left,right = 0, len(nums)-1
	while left<=right: #这里的等号容易漏掉
		mid = (left+right)//2
		if nums[mid] == target: #==不要打成=
			while mid+1<len(nums) and nums[mid+1]==target:
				mid += 1
			return mid+1 #这里的+1容易漏掉
		elif target < nums[mid]:
			right = mid - 1
		else:
			left = mid +1
	return left

slst = [7, 36, 53, 59, 61, 62, 73, 88, 97, 98]
print(slst)
print(search_insert(slst,target))
slst = [7, 25, 25, 25, 25, 25, 25, 25, 25, 25]
print(slst)
print(search_insert(slst,target))
for _ in range(10):
	slst = sorted([int(random.random()*N) for _ in range(k)])
	print(slst)
	print(search_insert(slst,target))