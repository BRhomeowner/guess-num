import random
r=random.randint(1,100)
while True:
	n=input('請輸入一個數字:')
	n=int(n)
	if n==r:
		print('恭喜你答對了!')
		break
	elif n!=r:
		if n>r:
			print('你猜的數字比較大')
		elif n<r:
			print('你猜的數字比較小')
