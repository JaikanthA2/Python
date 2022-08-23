calculation_to_units= 24
name_of_unit="hours"

def days_to_units(num_of_days):
        return (f"{num_of_days} days are  {num_of_days * 24} {name_of_unit}")

def validate_and_execute():
     try:
       user_input_number = int(num_of_days_element)
       if user_input_number > 0:
        my_result= days_to_units(user_input_number)
        print (my_result)
       elif user_input_number == 0:
        print(f"Zero is not valid enter positive number")
       else:
        print("Input is not a number")
     except:
         print("Not Valid Enter the correct number")

user_input= ""
while user_input != "exit":
    user_input= input("Enter user input number of days ")
    list_of_days=user_input.split(", ")
    
    print(list_of_days)
    print(set(list_of_days))

    print (type(list_of_days))
    print (type(set(user_input.split(", "))))

    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()

# The return keyword is placed in the function which return the value and store in the varible my_result and print 