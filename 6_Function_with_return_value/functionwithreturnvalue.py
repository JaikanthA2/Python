calculation_to_units= 24
name_of_unit="hours"

user_input= input("Enter user input number of days\n")
user_input_number=int(user_input)

print (user_input)
def days_to_units():
    return  (f"{user_input_number} days are  {user_input_number * 24} {name_of_unit}")

my_result= days_to_units()
print (my_result)


# The return keyword is placed in the function which return the value and store in the varible my_result and print 