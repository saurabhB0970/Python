# User-defined decorator
def addition_decorator(add):
    def wrapper(a, b):
        print("Start of addition")
        result = add(a, b)
        print("End of addition")
        return result
    return wrapper

# Function using the decorator
@addition_decorator
def add(a, b):
    print(f"The sum is: {a + b}")
    return a + b

# Call the function
add(5, 3)
