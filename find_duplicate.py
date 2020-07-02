from typing import List
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		# for i in range(len(nums)):
		# 	if nums[i] in nums[i+1:]:
		# 		return nums[i]
		seen = []
		for i in nums:
			if i in seen:
				return i
			else:
				seen.append(i)
lst = [1,3,4,2,2]
print(Solution().findDuplicate(lst))