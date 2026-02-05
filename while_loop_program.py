# Initialize the user's choice to an empty string to start the loop
user_input = ""

print("--- AI-Assisted Simple Calculator ---")
print("Enter 'exit' at any time to quit.")

# The 'while' loop is used because we don't know how many times 
# the user will want to calculate. It repeats indefinitely 
# until the condition (user_input != 'exit') becomes false.
while user_input.lower() != 'exit':
    
    user_input = input("\nEnter an equation (e.g., 5 + 5) or 'exit': ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break # Immediately exits the loop

    try:
        # eval() is a quick way to calculate string-based math.
        # In a real-world app, we'd add more safety checks here!
        result = eval(user_input)
        print(f"Result: {result}")
    except Exception as e:
        print("Oops! Please enter a valid math expression.")