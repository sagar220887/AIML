# Notebook1

while True:
	try:
		number = int(input('What is your weight?\n'))
		print('You should drink this much water in a day: ', (number/10) + 2)
		# print(18/number)
	except ValueError:
		print("\nonly numbers are allowed")
	# except ZeroDivisionError:
	# 	print("\nZeros are note allowed\n")
	except Exception as e:
		print(e)

	finally:
		print("Please send the next person")

