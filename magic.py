def updateA(a, x ,i):
	a[i] = a[i] + x
	a[i+1] = a[i+1] + 2*x
	a[i+2] = a[i+2] + 3*x
	
def check(a,b):	
	for i in range(len(a)-2):
		x = b[i] - a[i]
		if (x < 0):
			return "NIE"
		else:
			updateA(a, x , i)
	if (a == b ):
		return "TAK"
	else:
		return "NIE"
		
o=int(input())
for i in range(o):
	p=int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(check(a,b))
