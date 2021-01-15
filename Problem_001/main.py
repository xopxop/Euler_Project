# Problem 01:
# If we list all the natural number below 10 that are multiples of 3 or 5, we get 3, 5, 6, 9.
# The sum of these multiples is 23. Find and sum of all the multiples of 3 or 5 below 1000

def main():
	solution = 0
	x = range(1, 1000)
	for i in x:
		if i % 3 == 0 or i % 5 == 0:
			solution += i
	print(f'Solution: {solution}')

if __name__ == "__main__": main()