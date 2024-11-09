import random

# User dictionary whare user can under stand game easely
userChoice = {
    "r":0,
    "p":1,
    "s":-1
}

# Computer dictionary
computerChoice = {
    0:"r",
    1:"p",
    -1:"s"
}

user = input("Enter choice: ")

# randomaly occure value from list
computer = random.choice([0, 1, -1])

# Show User choice and computer randomaly selected value
print(f"AI choice: {computerChoice[computer]} \n User choice: {user}")

# Draw when both select same value
if computer == userChoice[user]:
    print("Draw Game")

# r 0 == p 1 ==> 1
#   0 ==   1 ==> 1
elif computer == 0 and userChoice[user] == 1:   #1
    print("YOU WIN")
    
# r 0 == s -1 ==> 0
#   0 ==   -1 ==> 0
elif computer == 0 and userChoice[user] == -1:  #0
    print("YOU LOSS")
    
# p 1 == r 0 ==> 1
#   1 ==   0 ==> 1
elif computer == 1 and userChoice[user] == 0:   #1
    print("YOU LOSS")
    
# p 1 == s -1 ==> -1
#   1 ==   -1 ==> -1
elif computer == 1 and userChoice[user] == -1:  #-1
    print("YOU WIN")
    
# s -1 == p 1 ==> -1
#   -1 ==   1 ==> -1
elif computer == -1 and userChoice[user] == 1:  #-1
    print("YOU LOSS")
    
# s -1 == r 0 ==> 0
#   -1 ==   0 ==> 0
elif computer == -1 and userChoice[user] == 0:  #0
    print("YOU WIN")

else:
    print("Wrong Choice!!!")


