database = [
	['ouxiao', '123'],
	['ou', '123'],
	['xiao', '456'],
	['cloudox', '123456']
]

username = raw_input('User name: ')
password = raw_input("Password: ")

if [username, password] in database: print 'Login!'
else: print 'Wrong!'