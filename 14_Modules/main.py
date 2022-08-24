#To import all fromt other py file
import helper

#To import all from other py file. The below one we not want to give the python file name while calling the function eg 
from helper import *

#renaming module
import helper as h
#to import only particular function from other py file
from helper import validate_and_execute,user_input_message

user_input= ""
while user_input != "exit":
    user_input= input(helper.user_input_message )
    days_and_unit=user_input.split(":")
    
    print(days_and_unit)
    days_and_unit_dictionary= {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary) #here we didn't use helper.validate_and_execute() this is due to import helper using *
#There are some bulit in modules also example os module, Logging module