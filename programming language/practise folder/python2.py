print("Help! My computer doesn't work!")
done = False
while not done:
	print("Does the computer make any sounds (fans , etc.)")
	choice = input("or show any lights? (y/n):\n")
	#the troubleshooting logic
	if choice == 'n' or 'N':
		choice = input("Is it plugged in(y/Y/n/N):")
		if choice == 'n' or 'N':
			print("Plug it in. ")
		else:
			print("Turn it on\n\t")
		else: