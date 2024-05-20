import numpy as np
s=2
r=2
m=4

p=np.array([[9,7,8],[5,4,6],[7,8,7],[4,6,3]])
test=np.array([[3,9,4]])
t=[1,0,1,0]
w=np.array([[-10,8,5]])
b= 20
a=0
k=0
while True:
	d=True
	k+=1
	print("lan lap thu ",k)

	for i in range(4):
		x=np.array([p[i]])
		n=w.dot(x.T)+b

		if n<0:
			a=0
		else :
			a=1

		if(np.array_equal(t[i],a)==False):
			e=t[i]-a
			w=w+np.dot(e,x)
			b=b+e
			d=False
	print("w=",w)
	print("b=",b)
	if(d==True):
		break


n=w.dot(test.T)+b
if n<0:
	wr="0"
else :
	wr="1"

print("Voi x1=3,x2=9,x3=4=>thuoc lop "+"\""+wr+"\"")
print("n",n)