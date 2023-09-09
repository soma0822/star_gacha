with open('notcomma', 'r') as file:
	content = file.read()

	contents = content.split(' ')
	for content in contents:
		print(content)
