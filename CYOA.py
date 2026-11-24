import time

print("\nWelcome to CaoCao's Restaurant where you get to have the dinner of your lifetime!")
n = input("We need the name on reservation, what is it?: ")

print(f"\nWelcome {n}! What drink do you want to start off?, option 1 or 2?")
print("1. Sodie pop")
print("2. Water")

choice = input("Make your choice!: ")

if choice == "1":
    print("\nyou enjoy a fresh cracking sodie pop.\n")

elif choice == "2":
    print("\nyou enjoy a refreshing glass of water.\n")

else:
    print("\nGame Over! You did not pick a given option.\n")
    quit()

time.sleep(1)

print("Now let's get you started with appetizers, would you like option 1 or 2?")
print("1. Quesadilla?")
print("2. Bandera Bread?")

choice1 = (input("Make your choice!: "))

if choice1 == "1":
    print(f"\n\"Good choice {n}, for it is a staple at CaoCao's Restaurant! Eat up!\"")
    print("\nThe quesadilla had too many beans in it! You slowly fill up with gas and explode.\n")
    print("Game Over!\n")
    quit()

elif choice1 == "2":
    print("\nYes, let's start you off with a banderea bread, good choice!\"")
    print("\nYou eat a hot steaming bandera bread, savouring every cheesy bite before your main course!.\n")

else:
    print("\nGame Over! You did not pick a given option.\n")
    quit()

time.sleep(1)

print(f"Woohoo! It's time for the main course. What do you want to eat for your main course? well, {n}?")
print("We have two special options for you today, would you like option 1 or 2!")
print("1. Beef Lagman")
print("2. Super Chilli Heat Lamian\n")

choice3 = input("Make your choice!: ")

if choice3 == "1":
    print("\nyum yum yum!!! The beef lagman is the best thing you've ever eaten, well...ever!")

elif choice3 == "2":
    print("\ncrap! The super chilli heat lamian was hot as hell! you go throw up in the bathroom and DIE!!!!")
    print("\nGame Over! It was too spicy...")
    quit()

else:
    print("\nGame Over! You did not pick a given option.")


time.sleep(1)

print("Looks like you cleaned your plate! Enjoyed that lagman did you? do you have room for dessert?")
print("Very good! option 1 or 2")
print("1. Banana Split")
print("2. Panookie")

choice4 = input("Make your choice!: ")

if choice4 == "1":
    print("\nYou watch as the dish comes out, you notice the banana looks oddly gun shaped. The banana IS actually a gun and the waiter shoots you in the head!")
    print("\nGame Over! The waiter was an evil assassin!\n")
    quit()

elif choice4 =="2":
    print("\nThe panookie comes out steaming in your face! The chocolaty goodness all up in your face.")
    print("You take your first bite and let the waiter know it's pertinent you give your compliments to the chef.")
    print("You leave the restaurant with a full belly and a happy smile")
    print("\nYou Win!\n")

else:
    print("\nGame Over! You did not pick a given option.\n")