tile = (1,1)
while True:
    direction_input = "q"
    if tile == (1,1):
        print("You can travel: (N)orth.")
        while direction_input not in "n":
            direction_input = input("Direction: ").lower()
            if direction_input == "n":
                tile = (1,2)
            else:
                print("Not a valid direction!")
    elif tile == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        while direction_input not in "nes":
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
        while direction_input not in "es":
            direction_input = input("Direction: ").lower()
            if direction_input == "e":
                tile = (2,3)
            elif direction_input == "s":
                tile = (1,2)
            else:
                print("Not a valid direction!")
    elif tile == (2,1):
        print("You can travel: (N)orth.")
        while direction_input not in "n":
            direction_input = input("Direction: ").lower()
            if direction_input == "n":
                tile = (2,2)
            else:
                print("Not a valid direction!")
    elif tile == (2,2):
        print("You can travel: (S)outh or (W)est.")
        while direction_input not in "ws":
            direction_input = input("Direction: ").lower()
            if direction_input == "w":
                tile = (1,2)
            elif direction_input == "s":
                tile = (2,1)
            else:
                print("Not a valid direction!")
    elif tile == (2,3):
        print("You can travel: (E)ast or (W)est.")
        while direction_input not in "ew":
            direction_input = input("Direction: ").lower()
            if direction_input == "e":
                tile = (3,3)
            elif direction_input == "w":
                tile = (1,3)
            else:
                print("Not a valid direction!")
    elif tile == (3,2):
        print("You can travel: (N)orth or (S)outh.")
        while direction_input not in "ns":
            direction_input = input("Direction: ").lower()
            if direction_input == "n":
                tile = (3,3)
            elif direction_input == "s":
                tile = (3,1)
            else:
                print("Not a valid direction!")
    elif tile == (3,3):
        print("You can travel: (S)outh or (W)est.")
        while direction_input not in "sw":
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
