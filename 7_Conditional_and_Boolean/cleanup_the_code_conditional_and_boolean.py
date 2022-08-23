calculation_to_units= 24
name_of_unit="hours"

def days_to_units(user_input_number):
    condition_check = user_input_number > 0
    print(type(condition_check))
    condition_datatype= type(user_input_number)
    if user_input_number > 0:
        return (f"{user_input_number} days are  {user_input_number * 24} {name_of_unit}")
    elif user_input_number == 0:
      return (f"{user_input_number} is not valid")
    else:
        return (f"{user_input_number} Invalid entry")

def validate_and_execute():
    if user_input.isdigit():
     user_input_number=int(user_input)
     my_result= days_to_units(user_input_number)
     print (my_result)
    else:
     print("Input is not a number")

user_input= input("Enter user input number of days\n")
validate_and_execute()
# The return keyword is placed in the function which return the value and store in the varible my_result and print 