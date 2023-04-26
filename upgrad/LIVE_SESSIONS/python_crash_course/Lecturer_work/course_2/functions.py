def dollar_inr(dollar):
	amount = dollar*82.27
	# print(amount)
	return amount


while True:
	try:
		user_input = int(input('enter the amount: '))
		output = dollar_inr(user_input)
		print("conversion is this much: ", output)
		break
	except ValueError:
		print("\nonly numbers are allowed")
# 	# except ZeroDivisionError:
# 	# 	print("\nZeros are note allowed\n")


# if __name__ == "__main__":
# 	dollar_inr(25)
