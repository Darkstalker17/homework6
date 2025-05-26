#Program to calculate the number of digits entered by the user
n = input("Enter a number: ")
if n.isdigit():
    print("The number of digits in the number is: ", len(str(n)))
else:
    print("This is not a number")