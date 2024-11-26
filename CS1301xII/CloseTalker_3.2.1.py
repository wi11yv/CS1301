item = "quesadilla"
meat = "steak"
queso = False
guacamole = False
double_meat = False


#-----------------------------------------------------------
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Let's further expand our previous program to cover a broader
#menu variety. Instead of just burritoes, now the program
#should cover three menu items: quesadillas, burritoes, and
#nachos. Instead of separate booleans for steak and pork,
#we instead have a string that could be "steak", "pork",
#"chicken", "tofu", and "beef". We still have booleans for
#queso and guacamole, but we also have a boolean for double
#meat.
#
#Your code should calculate the price as follows:
#
# - The base price for a quesadilla is 4.00, for nachos is
#   4.50, and for burritoes is 5.00.
# - If meat is steak or pork, add 0.50. Any other meat adds
#   no money to the price.
# - guacamole always adds 1.00 to the price.
# - queso adds 1.00 to the price UNLESS the item is nachos,
#   in which case it adds nothing.
# - double_meat adds 1.50 if the meat is steak or pork, or
#   1.00 otherwise.
base_price = 4.0
if item == "nachos":
    base_price = 4.5
if item == "quesadilla":
    base_price = 4.0
if item == "burrito":
    base_price = 5.0
    
if meat == "steak" or "pork":
    base_price += 0.50
if double_meat and "steak" or "pork":
    base_price += 1.50
elif double_meat and "chicken" or "tofu" or "beef":
    base_price += 1.00

if guacamole:
    base_price += 1.0

if queso and not "nachos":
    base_price += 1.0
    
print(base_price)




