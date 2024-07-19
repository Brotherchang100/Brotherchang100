import time

# Test1 

print(33)
print("ABC")
print (22+33)
A=50
print (A)

# Function to display the current time
def display_time():
    current_time = time.strftime("%H:%M:%S")
    print("Current time:", current_time)

# Call the function to display the time
display_time()

# Function to calculate the addition of two numbers
def add_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print("The sum is:", result)

# Call the function to calculate the addition
add_numbers()


