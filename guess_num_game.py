import random
r = random.randint(1,100)
count = 0

while True:
	num = input('請猜數字:')
	num = int(num)
	count += 1 # count = count + 1
	if num == r:
		print('終於猜對了!')
		print('你猜了', count, '次才猜對!')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	else:
		print('請輸入數字')
	print('這是你猜的第', count, '次')
