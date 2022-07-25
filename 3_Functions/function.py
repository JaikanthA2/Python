print (f"20 days are {20*24*60} minutes")



print (f"20 days are {20*24*60*60} seconds")

calculation_to_units= 24
name_of_unit="hours"

print (f"20 days are {20* calculation_to_units} {name_of_unit}")
print (f"30 days are {30* calculation_to_units} {name_of_unit}")
print (f"40 days are {40* calculation_to_units} {name_of_unit}")

def days_to_units():
    print ("=====================================")
    print("Inside the function days_to_units")
    print (f"50 days are {20* calculation_to_units} {name_of_unit}")
    print ("Executing the function days_to_units")
    print("=======================================")

days_to_units()