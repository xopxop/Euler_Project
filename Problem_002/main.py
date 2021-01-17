def main():
	solution = 0
	x = fibonacci_generator(4000000)
	for i in x:
		print(i)
		if i % 2 == 0: solution += i
	print(f'solution: {solution}')

def fibonacci_generator(stop):
	num1 = 1
	num2 = 2
	yield num1
	yield num2
	while num1 + num2 <= stop:
		if num2 > num1:
			num1 += num2
			yield num1
		elif num1 > num2:
			num2 += num1
			yield num2


if __name__ == '__main__': main()