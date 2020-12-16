number = -4

while(number < 1):
  number = int(input("Enter a natural number: "))

name = input("Enter your name: ")

if(number < 10):
  counter = 0
  printTimes = (2*number)
  space = " "
  spaceTimes = 0
  while(counter < printTimes):
    print(space*spaceTimes, end=" ")
    print(name)
    spaceTimes = spaceTimes + 4
    counter = counter + 1
  
else: 
  print(name*number, end="\n")