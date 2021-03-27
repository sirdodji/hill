print("Please enter an integer number")
a = input()
number = int(a)
b = str(number)
c = 1
next = int(c)
nextnumber = next + number
nextnumberbutstr = str(nextnumber)
previousnumber = number - next
previousnumberbutstr = str(previousnumber)
print("The next number for the number " + b + " is " + nextnumberbutstr)
print("The previous number for the number " + b + " is " + previousnumberbutstr)