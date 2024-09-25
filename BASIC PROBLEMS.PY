//CALCULATING SPEED

d=float(input('enter distance in kilometer:'))
t=float(input('enter time in minutes:'))
speed=d/t
print('speed',speed)


//CALCULATION OF GRADES

a=float(input('enter marks:'))
if a>=90:
	print('A grade')
elif a>=80 and a<90:
	print('B grade')
elif a>=70 and a<80:
	print('C grade')
elif a>60 and a<70:
	print('D grade')
elif a>=50 and a<60:
	print('E grade')
else:
	print('CANDIDATE IS FAILED')


//CELCIUS TO FAREHNHEAT

f=float(input('enter the tempereture:'))
c=5/9*(f-32)
print('temperature in celcius',c)

//CHECKING GIVEN ALPHABET VOWEL OR CONSONANT

ch=input('enter an alphbet:')
v=['a','e','i','o','u','A','E','I','O','U']

//EVEN OR ODD


a=int(input('enter a value:'))
b=a%2
if b==1:
	print('a is odd number')
else:
	print('a is even number')
if ch in v:
	print('ch is an vowel')
else:
	print('ch is a consonant')


//COMPOUND INTREST

p=float(input('enter principle amount:'))
t=float(input('enter time:'))
r=float(input('enter rate of intrest:'))
totalamount=(p*t*r)/100
print(totalamount)


//LEAP YEAR

a=int(input('enter an year:'))
if a%100!=0 and a%4==0:
	print('a is a leap year')
else:
	print('a is not a leap year')



//PATTERN PRINTING
n=int(input("enter the value of n:"))
i=1
j=i+1
for i in range(1,n+1):
	for j in range(1,i+1):
		print("* ",end=" ")
	print("")


//sum and average of digits

n=int(input("enter the value of n"))
a=[]
for i in range(n):
	ele=int(input("enter an element"))
	a.append(ele)
print(a)

print(sum(a)/len(a))


//reverse of digits
n=int(input("enter the values of n"))
a=[]
for i in range(n):
	ele=int(input("enter the values of elements"))
	a.append(ele)
print(a)
a.reverse()
print(a)


//min and max of index
n=int(input("enter n"))
a=[]
for i in range(n):
	ele=int(input("enter elements"))
	a.append(ele)
print(a)
print(a.index(max(a)))
print(a.index(min(a)))
