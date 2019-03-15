import os

options = {'port':'80','list_of_diapasons':'~/ips','output':'~/scan'}
options_ = ['port','list_of_diapasons','output']
print('\n\n\033[96m===>\033[00m \033[92m$CITYSCAN\033[00m \033[96m<===\033[00m')
print('\n\n\033[37m-------------------\033[00m\n\n')
while True:
	command = input('\033[32m==>\033[00m')
	if command == "help" or command == "help ":
		print('* \033[94mshow options\033[00m')
		print('* \033[94mset\033[00m [attribute] [value]')
		print('* \033[94mscan\033[00m')
	elif command == "show options" or command == "show options ":
		print('\033[34menter \'set\' to change options\033[00m')
		print('\033[95mport:\033[00m ' + options['port'])
		print('\033[95mlist_of_diapasons:\033[00m ' + options['list_of_diapasons'])
		print('\033[95moutput:\033[00m ' + options['output'])
	elif command[:3] == 'set':
		argv = []
		com = ''
		for _ in command:
			if _ == ' ':
				argv.append(com)
				com = ''
				continue
			com = com + _
		if com != '':
			argv.append(com)
		else:
			com = com
		if len(argv) != 3 or argv[1] not in options_:
			print('incorrect input')
		else:
			options[argv[1]] = argv[2]
	elif command == 'scan' or command == 'scan ':
		os.system('masscan -p' + options['port'] + ' -iL ' + options['list_of_diapasons'] + ' -oL ' + options['output']) 					
	else:
		print('\033[34menter \'help\' to show list of commands\033[00m')
