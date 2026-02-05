# Define the number we want to multiply
number = 7

print(f"Multiplication Table for {number}:")
print("-" * 20)

# We use a 'for loop' here because we know exactly how many times 
# we need to repeat the action (10 times). 
# range(1, 11) starts at 1 and stops BEFORE 11.
for i in range(1, 11):
    result = number * i
    # This prints the step-by-step calculation
    print(f"{number} x {i} = {result}")

# Why use a for loop?
# 1. Efficiency: It replaces 10 lines of manual code with just 2 lines.
# 2. Scalability: If you want to print 1,000 rows, you only change '11' to '1001'.
# 3. Readability: It clearly shows the intent to iterate through a sequence.