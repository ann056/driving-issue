driving = input('你有沒有開過車？')
if driving != '有' and '沒有':
	print('請輸入有/沒有')
	raise SystemExit
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('開車小心！')
	else:
		print('奇怪...你怎麼會開過車？')
if driving == '沒有':
	if age >= 18:
		print('你可以考駕照了啊')
	else:
		print('乖乖等到18歲再去考駕照吧')
