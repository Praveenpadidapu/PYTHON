n=int(input("enter the number:"))
f1=0
f2=1
for i in range(1,n+1):
	print(f1)
	f3=f1+f2
	f1=f2
	f2=f3


//fabinocci series using for loop

n=int(input("enter the value of n"))
n1=0;
n2=1;
for i in range(n1,n):
    n=n1+n2;
    n2=n1;
    n1=n;
    print(n2);

//fabinocci series upto user given range by for loop

n=int(input("enter the  upto range value of series: n"))
n1=int(input("enter the starting  value of series :n1"))
n2=int(input("enter the value of n2"))
for i in range(n1,n):
    n=n1+n2;
    n2=n1;
    n3=n;
    print(n);
