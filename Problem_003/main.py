# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143

def main():
	factors = find_factor(600851475143)
	solution = find_largest_prime(factors)
	print(f'solution: {solution}')

def find_factor(value):
	ret = []
	i = 2
	while value != 1:
		if value % i == 0:
			ret.append(i)
			value = value // i
		i += 1
	return ret

def find_largest_prime(o):
	max = 0
	for i in o:
		if isPrime(i): max = i
	return max

def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

if __name__ == '__main__': main()