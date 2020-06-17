class Solution:
	def generate(self,row_num):
		if row_num == 0:
			return []
		elif row_num == 1:
			return [[1]]
		else:
			triangle = self.generate(row_num-1)
			new_row = [1] + [triangle[-1][i]+triangle[-1][i+1] for i in range(row_num-2)] + [1]
			triangle.append(new_row)
		return triangle
results = Solution().generate(10)
for res in results:
	print(res)