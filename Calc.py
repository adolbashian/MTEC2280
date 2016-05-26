def calculate():
	print("PyCalculator V1.0")
	while(True):
		x = raw_input("(5 for Quit) 1. Add, 2. Subtract 3. Multiply 4. Divide")
		if(int(x) == 1):
			valueA = raw_input("First value to add")
			valueB = raw_input("Second value to add")
			v = int(valueA) + int(valueB)
			print("Added Value is %i" % v)

		elif(int(x) == 2):
			valueA = raw_input("First value to subtract")
			valueB = raw_input("Second value to subtract")
			v = int(valueA) - int(valueB)
			print("Added Value is %i" % v)

		elif(int(x) == 3):
			valueA = raw_input("First value to multiply")
			valueB = raw_input("Second value to multiply")
			v = int(valueA) * int(valueB)
			print("Added Value is %i" % v)

		elif(int(x) == 4):
			valueA = raw_input("First value to divide")
			valueB = raw_input("Second value to divide")
			v = int(valueA) / int(valueB)
			print("Added Value is %i" % v)

		elif(int(x) == 5):
			print("Exiting")
			return 0

		else:
			print("Invalid Input")

calculate()
