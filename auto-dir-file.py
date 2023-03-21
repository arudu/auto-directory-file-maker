import os

MESSAGE = "The directory already exists."
try:
	home = os.path.expanduser(
		input("What would you like to name this directory?  ")
	)
	print("The new directory name is " + home)

	FILENAME = input("Whats the name of the file  ")

	if not os.path.exists(
		os.path.join(home, FILENAME)
	):
		os.makedirs(
			os.path.join(home, FILENAME)
		)
	else:
		print(MESSAGE)
except Exception as e:
	print(e)
