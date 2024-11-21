hot = True
cold = False
morning = True
evening = False
night = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a program that will recommend a beverage based on the
#current weather and time of day. Specifically, the program
#should recommend:
#
# - coffee if it's morning, or if it's cold and evening
# - hot tea if it's cold and either evening or night
# - smoothie if it's hot, no matter what time of day it is
# - milkshake if it's hot and evening, or if it's night
#   no matter the temperature
#
#Write some code below that will print four lines, one for
#each of the four beverages. The lines should look like this:
#
#Coffee: True
#Hot Tea: False
#Smoothie: True
#Milkshake: True
#
#The values (True and False) will differ based on the
#values assigned to hot, cold, morning, evening, and night
#at the start of the program.


#Add your code here!
coffee = morning or (cold and evening)
tea = cold and (evening or night)
smoothie = hot
milkshake = (hot and evening) or (night)


print("Coffee: {0}\nHot Tea: {1}\nSmoothie: {2}\nMilkshake: {3}".format(coffee, tea, smoothie, milkshake))






