#In the code below, four variables are created:
#an integer, a float, a date, and a boolean.
#
#Create four new variables: integer_as_string,
#float_as_string, date_as_string, and
#boolean_as_string.
#
#Convert the corresponding variables to strings.
#So, boolean_as_string should have the string
#version of the current value of new_boolean.

from datetime import date
new_integer = 8
integer_as_string = str(new_integer)

new_float = 8.2
float_as_string = str(new_float)

new_date = date.today()
date_as_string = str(new_date)

new_boolean = False
boolean_as_string = str(new_boolean)

#The lines of code below will test your code.
#If it works, they will print the four string
#values, each followed by "<class 'str'>".
print(integer_as_string, type(integer_as_string))
print(float_as_string, type(float_as_string))
print(date_as_string, type(date_as_string))
print(boolean_as_string, type(boolean_as_string))