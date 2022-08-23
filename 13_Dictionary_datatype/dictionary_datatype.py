
def days_to_units(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return (f"{num_of_days} days are  {num_of_days * 24} hours")
    elif conversion_unit == "minutes":
         return (f"{num_of_days} days are  {num_of_days * 24 * 60 } minutes")
    else:
        return ("Unsupported Unit")

def validate_and_execute():
     try:
       user_input_number = int(days_and_unit_dictionary["days"])
       if user_input_number > 0:
        my_result= days_to_units(user_input_number,days_and_unit_dictionary["unit"] )
        print (my_result)
       elif user_input_number == 0:
        print(f"Zero is not valid enter positive number")
       else:
        print("Input is not a number")
     except:
         print("Not Valid Enter the correct number")

user_input= ""
while user_input != "exit":
    user_input= input("Enter user input number and the conversion unit ")
    days_and_unit=user_input.split(":")
    
    print(days_and_unit)
    days_and_unit_dictionary= {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()

# The return keyword is placed in the function which return the value and store in the varible my_result and print 