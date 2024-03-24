n = int(input("Enter the upper limit for prime number generation: "))
primes = [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
for prime in primes:
  print(prime)

# Generate list of non-primes (composite numbers)
composites = [num for num in range(2, n + 1) if not all(num % j != 0 for j in range(2, int(num**0.5) + 1))]

# Print composite numbers
for composite in composites:
  print(composite)
