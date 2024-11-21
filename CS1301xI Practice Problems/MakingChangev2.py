total = "5.45"
cash = "10.0"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you're writing the code for a cash register. As part
#of this, it will have a total price for a purchase, and an
#amount of cash the buyer is paying. However, both of these
#are represent as strings.
#
#Write some code that will find and print the change that the
#customer is due. For example, if cash is 10.0 and total is
#5.45, then the change would be 4.55.
#
#Then, print the result with a message like this: "Your
#change is: 4.55". Do not include the quotes in your output.
#You may assume total and cash will both be floats.


#Add your code here!

change = float(cash) - float(total)

print("Your change is:", change)