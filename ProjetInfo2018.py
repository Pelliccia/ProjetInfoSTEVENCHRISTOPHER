import numpy

a=-3
b=9
c=-5
d=2

y= lambda x: a*numpy.sin(x**4)+b*x**2+c*x+numpy.log10(d*x**2)+numpy.random.normal(0,0.35)

xlist=numpy.random.uniform(0.1,10,50)

def ylist(llist,f):
	length=len(llist)
	out=[]
	for i in range (0,length):
		out.append(f(llist[i]))
	return out

def Average(llist):
        length=len(llist)
        out=0
        for i in range (0,length):
                out=out+llist[i]
        out=out/length
        return out

AvgX=Average(xlist)
AvgY=Average(ylist(xlist,y))

def Difference(llist):
        length=len(llist)
        out=[]
        avg=Average(llist)
        for i in range (0,length):
                out.append(llist[i]-avg)
        return out

XDiff=Difference(xlist)
YDiff=Difference(ylist(xlist,y))




