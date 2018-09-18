tile = (1,1)
while True:
    if tile == (1,1):
        print("You can travel: (N)orth.")
        direction_input = input("Direction: ").lower()
        if direction_input == "n":
            tile = (1,2)
        else:
            print("Not a valid direction!")
            return
    elif tile == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction_input = input("Direction: ").lower()
        if direction_input == "n":
            tile = (1,3)
        elif direction_input == "e":
            tile = (2,2)
        elif direction_input == "s":
            tile = (1,1)
        else:
            print("Not a valid direction!")
    elif tile == (1,3):
        print("You can travel: (E)ast or (S)outh.")
        direction_input = input("Direction: ").lower()
        if direction_input == "e":
            tile = (2,3)
        elif direction_input == "s":
            tile = (1,2)
        else:
            print("Not a valid direction!")
    elif tile == (2,1):
        print("You can travel: (N)orth.")
        direction_input = input("Direction: ").lower()
        if direction_input == "n":
            tile = (2,2)
        else:
            print("Not a valid direction!")
    elif tile == (2,2):
        print("You can travel: (W)est or (S)outh.")
        direction_input = input("Direction: ").lower()
        if direction_input == "w":
            tile = (1,2)
        elif direction_input == "s":
            tile = (2,1)
        else:
            print("Not a valid direction!")
    elif tile == (2,3):
        print("You can travel: (E)ast or (W)est.")
        direction_input = input("Direction: ").lower()
        if direction_input == "e":
            tile = (3,3)
        elif direction_input == "w":
            tile = (1,3)
        else:
            print("Not a valid direction!")
    elif tile == (3,2):
        print("You can travel: (N)orth or (S)outh.")
        direction_input = input("Direction: ").lower()
        if direction_input == "n":
            tile = (3,3)
        elif direction_input == "s":
            tile = (3,1)
        else:
            print("Not a valid direction!")
    elif tile == (3,3):
        print("You can travel: (S)outh or (W)est.")
        direction_input = input("Direction: ").lower()
        if direction_input == "s":
            tile = (3,2)
        elif direction_input == "w":
            tile = (2,3)
        else:
            print("Not a valid direction!")
    elif tile == (3,1):
        print("Victory!")
        break