print("enter number")
x = abs(int(float(input())))  #не уверен надо ли было округлять. но пусть будет
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
if x in numbers:
    print(x)
    print("number is in list")
else: print("this number doesnt exist")