principal = 40000
rate = 0.05
years = 5
goal = 50000

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The variables above represent the current status of an
#investment account. The variable principal represents the
#initial value of the account. The variable rate represents
#the interest rate. The variable years represents the number
#of years the account will be allowed to grow.
#
#The variable goal represents the amount of money the investor
#hopes to have saved up by the end of that time period.
#
#Add some code below that will calculate whether the
#investment described by the values above will meet the given
#goal. If it will, print True. If it will not, print False.
#
#The formula for the value of an account after a given time
#(in number of years) is:
#
#  Current Value = principal * e ^ (rate * number of years)
#
#Because of the next line, you may use the variable e to
#represent the value of e. For example, print(e * 2) would
#print 5.43656365691809, which is double the value of e.
from math import e


#Add your code here!
#  Current Value = principal * e ^ (rate * number of years)

value = principal * e ** (rate * years)
print(value >= goal)





