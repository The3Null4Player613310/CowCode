def uncow_main():
	data = ''
	while(True):
		try:
			line = input()
			for char in line:
				if (char in 'mo'):
					data += '0'
				if (char in 'MO'):
					data += '1'
		except:
			output = ''
			for char in range(0,int(len(data)/16)):
				output += chr(int(data[0:16],2))
				data = data[16:]
			print(output, end='')
			print('\0', end='')
			return

if (__name__ == '__main__'):
	uncow_main()
