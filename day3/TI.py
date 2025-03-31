print("welcome to the treasure island your mission is to find the treasure: ")
one = input("you have hit a wall, enter left or right: ")
if one.lower() == "left":
    two = input("swim or wait: ")
    if two.lower() == "wait":
        three = input("which door ? blue, yellow, red: ")
        if three.lower() == "yellow":
            print("you win")
        elif three.lower() == "red":
            print("burned by fire, game over")
        elif three.lower() == "blue":
            print("eaten by beasts, game over")
        else:
            print("Game over")
    else:
        print("Attacked by trout.Game Over")
else:
    print("Fall into a hole.Game Over.")
