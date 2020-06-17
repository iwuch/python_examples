class Solution():
	def fib(self,num):
		if num == 1 or num == 0:
			return num
		else:
			return self.fib(num - 1) + self.fib(num - 2)

for i in range(1,10):
	result = Solution().fib(i)
	print(result)