intervals = [[1,2],[3,4],[5,6],[0,10],[7,12]]
def merge(intervals):
	intervals.sort()
	results = []
	for i in intervals:
		if not results or results[-1][-1]<i[0]:
			results.append(i)
		else:
			results[-1][-1] = max(results[-1][-1],i[-1])
	return results

print(merge(intervals))