password = 'a123456'
i =3
while True:
	pwd = input("What's your password?: ")
	if pwd == password:
		print('You have been successfully logged in.')
		break
	else:
		i = i - 1
		print('Your password is incorrect. You still have ', i,' chances')
		if i == 0:
			break
			