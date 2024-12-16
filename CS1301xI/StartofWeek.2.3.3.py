donuts = 119

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#A donut shop sells donuts in four sizes: packs of 60 donuts,
#packs of 12 donuts, packs of 3 donuts, and individual donuts.
#
#To divide donuts into packs, they start by making as many of
#the largest pack as they can. Then, they make as many of the
#next largest pack, then the next pack, then finally they sell
#the remaining donuts individually. For example, if they baked
#119 donuts, then they would divide those donuts into one
#pack of 60, four packs of 12, three packs of 3, and 2
#individual donuts.
#
#Based on the variable donuts above, calculate how many of
#each size they will make. Print the results according to
#this template:
#
#Packs of 60: 1
#Packs of 12: 4
#Packs of 3: 3
#Packs of 1: 2


#Add your code here!

print("Packs of 60: {0}\nPacks of 12: {1}\nPacks of 3: {2}\nPacks of 1: {3}".format(donuts // 60, (donuts - (donuts // 60 * 60)) // 12, (donuts - ((donuts // 60 * 60) + (donuts // 12 * 12))) // 3, (donuts - ((donuts // 60 * 60) + (donuts // 12 * 12) + (donuts // 3 * 3))) // 1))
