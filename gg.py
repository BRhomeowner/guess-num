import random
start=input('請決定隨機數字範圍開始值:')
end=input('請決定隨機數字範圍結束值:')
start=int(start)
end=int(end)
r=random.randint(start,end)
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
