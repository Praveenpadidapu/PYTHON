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
