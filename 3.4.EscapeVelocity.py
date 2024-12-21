#Imagine you're writing the code to support the launch
#of an interstellar spacecraft, which can be launched
#from either earth or one of a number of other
#interstellar bodies. Each such body would have its own
#escape velocity.
#
#Depending on the use case, you may need to provide the
#escape velocity in terms of kilometers per second,
#kilometers per hour, miles per second, or miles per
#hour.
#
#Write a function called escape_velocity. escape_velocity
#should have one positional parameter, escape_velocity.
#escape_velocity represents the escape velocity in terms
#of kilometers per second.
#
#escape_velocity should also have two keyword parameters,
#in_kilometers and in_seconds, in that order. The default
#value for both should be True.
#
#Your function should return the escape velocity, rounded
#to two decimal points, converted to the desired units.
#
#If in_kilometers is False, you should convert the escape
#velocity from kilometers to miles by multiplying by 0.62.
#
#If in_seconds is False, you should convert the escape
#velocity from seconds to hours by multiplying by 3600.
#
#If both are False, you should perform both conversions.
#If both are True, you should return the original number
#rounded to two decimal places.
#
#Hint: Remember, you can round a number to two decimal
#places by using the round function. round(the_num, 2) will
#return the_num rounded to two decimal places.


#Add your code here!;
def escape_velocity(ev, in_kilometers = True, in_seconds = True):
    if not in_kilometers:
        ev *= 0.62
    elif not in_seconds:
        ev *= 3600
    elif in_kilometers and in_seconds:
        print(round(ev, 2))


    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#216.61
#134.3
#779796.0
#483473.52
print(escape_velocity(216.61))
print(escape_velocity(216.61, in_kilometers = False))
print(escape_velocity(216.61, in_seconds = False))
print(escape_velocity(216.61, in_kilometers = False, in_seconds = False))





