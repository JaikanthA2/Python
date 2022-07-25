calculation_to_units= 24
name_of_unit="hours"

def days_to_units(num_of_days):
    print ("=====================================")
    print("Inside the function days_to_units")
    print (f"{num_of_days} days are { num_of_days * calculation_to_units} {name_of_unit}")
    print ("Executing the function days_to_units")
    print("=======================================")

days_to_units(35)
days_to_units(45)
days_to_units(55)