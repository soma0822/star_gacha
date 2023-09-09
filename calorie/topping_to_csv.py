with open('topping_message', 'r') as file:
    content = file.read()

# 区切り文字（例: "---------------------------"）で分割する
sections = content.split('---------------------------')

sizes = ["Venti", "Grande", "Tall", "Short"]


for section in sections:
	messages = section.split('\n\n\n\n')

	for size in sizes:
	
		print(messages[0] + " " + size, end='')

		index = 1
		while True:
			if index >= len(messages):
				break
			one_messages = messages[index].split('\n\n')
			print(', ', end='')
			for one_message in one_messages:
				print(one_message + ' ', end='')
			index += 1
		print('\n')

		
			