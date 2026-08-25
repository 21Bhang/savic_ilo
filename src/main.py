from utils import square, is_even, celsius_to_fahrenheit

user_input = float(input("Enter a number: "))

num_squared = square(user_input)
num_is_even = is_even(user_input)
num_fahrenheit = celsius_to_fahrenheit(user_input)

print(f"The square of {num_squared}")
print(f"is even: {num_is_even}")
print(f"degrees Celsius is equal to {num_fahrenheit} degrees Fahrenheit.")