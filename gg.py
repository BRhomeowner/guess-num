import random
r=random.randint(1,100)
count=0
while True:
	count+=1
	n=input('請輸入一個數字:')
	n=int(n)
	if n==r:
		print('恭喜你答對了!')
		print('這是你猜的第',count,'次')
		break
	elif n!=r:
		if n>r:
			print('你猜的數字比較大')
		elif n<r:
			print('你猜的數字比較小')
		print('這是你猜的第',count,'次')
