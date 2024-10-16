def fibonacci_sequence(n):
    # Generate Fibonacci sequence up to n
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

def corresponding_fibonacci(input_seq):
    # Compute corresponding Fibonacci number for each element in the list
    max_number = max(input_seq)
    fib_sequence = fibonacci_sequence(max_number)
    
    output_seq = [fib_sequence[number] for number in input_seq]
    return output_seq

# Example usage
seq_a = [1, 2, 3, 4, 5, 6]
seq_b = corresponding_fibonacci(seq_a)
print(seq_b)