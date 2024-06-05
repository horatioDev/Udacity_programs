# Get Integer Input
def get_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid integer.")



# Get Positive Integer Input
def get_positive_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      if value <= 0:
        print("Please enter a positive integer.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid positive integer.")



# Get Float Input
def get_float_input(prompt):
  while True:
    try:
      value = float(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid float.")


# Get Positive Float Input
def get_positive_float_input(prompt):
  while True:
    try:
      value = float(input(prompt))
      if value <= 0:
        print("Please enter a positive float.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid positive float.")



# Get String Input
def get_string_input(prompt):
  while True:
    try:
      value = str(input(prompt))
      if value == '':
        value = None
      return value
    except ValueError:
      print("Invalid input. Please enter a valid string.")



# Get Boolean Input
def get_boolean_input(prompt):
  while True:
    user_input = input(prompt).strip().lower()
    if user_input == 'true':
        return True
    elif user_input == 'false':
        return False
    else:
        print("Invalid input. Please enter 'true' or 'false'.")


# Usage examples: -------------------------------------------------------------

# Integer ----------------------
# user_age = get_integer_input("Enter your age: ")
# print(f"Your age is: {user_age}")

# num_items = get_positive_integer_input("Enter the number of items (must be positive): ")
# print(f"You entered: {num_items}")

# Float --------------------------
# temperature = get_float_input("Enter the current temperature (e.g., 25.5): ")
# print(f"The temperature is: {temperature}")

# price = get_positive_float_input("Enter the price (must be positive): ")
# print(f"The price is: {price}")

# String ------------------------
# user_name = get_string_input("Enter your name: ")
# if user_name:
#   print(f"Hello, {user_name}!")
# else:
#   print("You didn't enter a name.")

# Boolean ------------------------
# is_approved = get_boolean_input("Are you approved? (Enter 'true' or 'false'): ")
# if is_approved:
#     print("You are approved!")
# else:
#     print("You are not approved.")

# End -------------------------------------------------------------------------