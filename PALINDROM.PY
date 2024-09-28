n=int(input("enter n value="))
i=n
sum=0
while n>0:
        rem=n%10
        sum=sum*10+rem
        n=n//10
if(sum!=i):
      print("it is not a palindrome")
else:
      print("it is a palindrome")        
