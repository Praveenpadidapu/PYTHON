n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n):
	if(n%i==0):
		sum=sum+i
print("sum=",sum)
if(sum==n):
	print("perfect number") 
else:
	print("not a perfect number")
