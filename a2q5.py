def mini(x):
	m=x[0]
	for i in range(1,len(x)):
		if x[i]<m:
			m=x[i]
	return m
from array import *
x=array('i',[])
n=int(input())
for i in range(0,n):
	a=int(input())
	x.append(a)
if n==0:
	print(x[0])
for i in range(1,n):
	min1=mini(x)
	x.remove(min1)
	min2=mini(x)
	x.remove(min2)
	a=(3*min1+2*min2)%100
	x.append(a)
print(x[0])