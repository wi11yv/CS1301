current_day = 12
current_month = 9
current_year = 2019
exp_day = 13
exp_month = 9
exp_year = 2019

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Given the current date and expiration date held by the
#variables above, determine whether a food with the listed
#expiration date has expired. Print True if it has expired,
#False is it has not. A food is defined as expired if the
#current date is _after_ the expiration date, not equal to
#it.


#Add your code here!
print((current_year > exp_year) or (current_year == exp_year and current_month > exp_month) or (current_year == exp_year and current_month == exp_month and current_day > exp_day))
