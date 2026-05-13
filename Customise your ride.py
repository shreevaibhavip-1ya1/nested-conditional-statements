print("Select your ride")
print("1. Bike")
print("2. Car")

# take input of number 1 or 2
# select your ride
choice = int(input("Enter your choice: "))

# User entering option 1
if( choice == 1 ): #condition 1 outer if statement
    print(" what type of a bike? ")
    print("1. TVS Jupiter\n")
    print("2. Mt 15\n")

# Condition for selecting the type of bike
    choice2 = int(input("Enter your choice2: "))
    if choice2==1: #inner if statement
      print("you have selected the TVS Jupiter")
    else:
     print("you have selected the Mt 15")

# User entering option 2
elif( choice == 2 ): #outer elif statement
 print(" what type of car?")
 print("1. Maruti Suzuki Dzire")
 print("2. Tata Punch")
 choice3=int(input("enter your choice3: "))

 if choice3==1: #inner if statement
#condition for selecting the type of car
   print(" you have selected the Maruti Suzuki Dzire")
 else: 
   print("you have selected the Tata Punch")
else: #outer else statement
 print("Wrong choice!")