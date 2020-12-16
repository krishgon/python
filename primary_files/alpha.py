number = -2

while(number < 1):
    number = int(input("Enter a natural number: "))

name = input("Enter your name: ")

if(number <= 10):
    print(name*(2*number))

else:
    print(name*number)