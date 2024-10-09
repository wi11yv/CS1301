parent_1 = "Caitlin"
parent_2 = "David"
baby = "Lucy"
month = "January"
day = 2
year = 2015
time = "11:12PM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The variables above give some information about a baby's birth:
#the names of the parents, the name of the baby, and the month,
#day, year, and time of the wedding.
#
#Add some code that will write the text to appear on a birth
#announcement based on these values. For the values shown above,
#this would read:
#
#Lucy was born to Caitlin and David at January 2, 2015 at 11:12PM.
#
#Note that all components of this statement are required: the
#baby's name, " was born to ", the first parent's name, " and ",
#the second parent's name," at ", the month, the day, a comma, the
#year, " at ", the time, and a period.
#
#HINT: Copy the sentence from above and replace the current values
#(Caitlin, David, January, etc.) with variables to reduce the
#risk of typoes throwing off your answers.


#Add your code here!

print("{0} was born to {1} and {2} at {3} {4}, {5} at {6}.".format(baby, parent_1, parent_2, month, day, year, time))








