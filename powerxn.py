# def pow(x,n):
# 	if n == 0:
# 		return 1
# 	if n >= 0:
# 		if n%2==1:
# 			return pow(x,n//2)**2*x
# 		else:
# 			return pow(x,n/2)**2
# 	else:
# 		return 1/pow(x,-n)

def pow(x,n):
	if not isinstance(n,int):
		return 'N is not an interger.'
	def cal(i):
		if i == 0:
			return 1
		root = cal(i//2)
		return root*root if i%2==0 else root*root*x
	return cal(n) if n>=0 else 1/cal(-n)
print(pow(2,5.5))

def test(x,n):
	if n == 1 or 0:
		return 1 if n == 0 else x
	else:
		root = test(x,n//2)
		return root*root if not n%2 else root*root*x
print(test(2,5))