import time

print("\nWelcome to CaoCao's Restaurant where you get to have the dinner of your lifetime!")
n = input("We need the name on reservation, what is it?: ")

print(f"\nWelcome {n}! What drink do you want to start off?, option 1 or 2?")
print("1. Sodie pop")
print("2. Water")

choice = input("Make your choice!: ")

if choice == "1":
    print("\nyou enjoy a fresh cracking sodie pop.\n")

if choice == "2":
    print("\nyou enjoy a refreshing glass of water.\n")

time.sleep(1)

print("Now let's get you started with appetizers, would you like option 1 or 2?")
print("1. Quesadilla?")
print("2. Bandera Bread?")

choice1 = (input("Make your choice!: "))

if choice1 == "1":
    print(f"\n\"Good choice {n}, for it is a staple at CaoCao's Restaurant! Eat up!\"")
    print("\nThe quesadilla had too many beans in it! You slowly fill up with gas and explode.\n")
    print("Game Over!")

if choice1 == "2":
    print("\nYes, let's start you off with a banderea bread, good choice!\"")
    print("\nYou eat a hot steaming bandera bread, savouring every cheesy bite before your main course!.\n")


    