def generate_fibonacci(n_terms):
    fibonacci_seq = []
    a, b = 0, 1

    for _ in range(n_terms):
        fibonacci_seq.append(a)
        a, b = b, a + b

    return fibonacci_seq

# Get user input
try:
    terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = generate_fibonacci(terms)
        print("Fibonacci sequence:")
        print(result)
except ValueError:
    print("Invalid input! Please enter an integer.")
