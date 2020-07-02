from typing import List
class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		max_length = 0
		length = 0
		for i in nums:
			# 神来之笔
			length = length*i + i
			# if i == 1:
			# 	length +=1
			# else:
			# 	length = 0
			if length > max_length:
				max_length = length
		return max_length

lst = [1,1,1,0,0,1,1,1,1,0,1,1,1,1,1]
print(Solution().findMaxConsecutiveOnes(lst))