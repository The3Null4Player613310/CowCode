l_moo = 'moo'
u_moo = 'MOO'

def cow_main():
	bit_index = 0
	while(True):
		try:
			line = input();
			line = line + '\n'
			for char in line:
				uni_bin = format(ord(char), '016b')
				for bit in uni_bin:
					moo_index = (bit_index % 3)
					if (bit == '0'):
						print(l_moo[moo_index], end='')
					elif (bit == '1'):
						print(u_moo[moo_index], end='')
					if (moo_index == 2):
						print(' ', end='')
					bit_index += 1
		except:
			print('\0', end='')
			return;

if (__name__ == '__main__'):
	cow_main()
