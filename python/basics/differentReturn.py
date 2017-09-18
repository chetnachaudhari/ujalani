def differentReturns(arg):
	if arg == 1:
		return "One"
	if arg == "One":
		return True

if __name__ == "__main__":
	print(differentReturns(1))
	print(differentReturns("One"))