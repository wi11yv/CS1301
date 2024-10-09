number = 1101

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The number above represents a binary number. It will always
#be up to eight digits, and all eight digits will always be
#either 1 or 0.
#
#The string gives the binary representation of a number. In
#binary, each digit of that string corresponds to a power of
#2. The far left digit represents 128, then 64, then 32, then
#16, then 8, then 4, then 2, and then finally 1 at the far right.
#
#So, to convert the number to a decimal number, you want to (for
#example) add 128 to the total if the first digit is 1, 64 if the
#second digit is 1, 32 if the third digit is 1, etc.
#
#For example, 00001101 is the number 13: there is a 0 in the 128s
#place, 64s place, 32s place, 16s place, and 2s place. There are
#1s in the 8s, 4s, and 1s place. 8 + 4 + 1 = 13.
#
#Note that although we use 'if' a lot to describe this problem,
#this can be done entirely boolean logic and numerical comparisons.
#
#Print the number that results from this conversion.


#Add your code here!

binary = str(number)
length = len(binary)
numeric_value = 0

numeric_value += (length > 0 and binary[-1] == "1") * 1
numeric_value += (length > 1 and binary[-2] == "1") * 2
numeric_value += (length > 2 and binary[-3] == "1") * 4
numeric_value += (length > 3 and binary[-4] == "1") * 8
numeric_value += (length > 4 and binary[-5] == "1") * 16
numeric_value += (length > 5 and binary[-6] == "1") * 32
numeric_value += (length > 6 and binary[-7] == "1") * 64
numeric_value += (length > 7 and binary[-8] == "1") * 128

print(numeric_value)



