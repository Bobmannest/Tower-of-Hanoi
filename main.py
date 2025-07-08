# Even num of disks = left option, Odd num of disks = right option
def odd_or_even(current_rod, rods):
    if len(rods[current_rod]) % 2 == 0:
        match current_rod:
            case 0:
                item_to_move = rods[0].pop()
                rods[1].append(item_to_move)
            case 1:
                item_to_move = rods[1].pop()
                rods[0].append(item_to_move)
            case 2:
                item_to_move = rods[2].pop()
                rods[0].append(item_to_move)
    else:
        match current_rod:
            case 0:
                item_to_move = rods[0].pop()
                rods[2].append(item_to_move)
            case 1:
                item_to_move = rods[1].pop()
                rods[2].append(item_to_move)
            case 2:
                item_to_move = rods[2].pop()
                rods[1].append(item_to_move)


# When current rod is 3 and needs to be +1, it should go back to rod 1 and vice versa
def current_rod_change(current_rod, decision):
    # Makes sure current_rod value doesn't go over 2 and under 0 as well
    if decision == "+":
        return (current_rod + 1) % 3
    elif decision == "-":
        return (current_rod - 1) % 3
    return None


# Checks if other rods are empty so an error does not occur
def left_rod_check(rods, current_rod):
    if not len(rods[(current_rod - 1) % 3]):
        return 99999
    else:
        return rods[(current_rod - 1) % 3][-1]


def right_rod_check(rods, current_rod):
    if not len(rods[(current_rod + 1) % 3]):
        return 99999
    else:
        return rods[(current_rod + 1) % 3][-1]


def current_rod_check(rods, current_rod):
    if not len(rods[current_rod]):
        return 99999
    else:
        return rods[current_rod][-1]


# Solves a new game of Tower of Hanoi
def basic_solve(disk_count):
    rods = [[], [], []]
    current_rod = 0

    #Builds starting layout
    new_disk_count = disk_count
    for _ in range(disk_count):
        rods[0].append(new_disk_count)
        new_disk_count -= 1
    print("Left rod:  ", rods[0], "\nMiddle rod:", rods[1], "\nRight rod: ", rods[2], "\n")

    # Each move
    while len(rods[2]) < disk_count:
        move_count = 0
        for _ in range(2):
            left_check = left_rod_check(rods, current_rod)
            current_check = current_rod_check(rods, current_rod)
            right_check = right_rod_check(rods, current_rod)

            if current_check < left_check or current_check < right_check:
                move_count += 1
                odd_or_even(current_rod, rods)
                print("Left rod:  ", rods[0], "\nMiddle rod:", rods[1], "\nRight rod: ", rods[2], "\n")

        # If prior to current turn 1 move was made, current rod moves in one order
        if move_count == 1:
            # Even
            if disk_count % 2 == 0:
                current_rod = current_rod_change(current_rod, "-")
            # Odd
            else:
                current_rod = current_rod_change(current_rod, "+")
        # If prior to current turn 1 move was made, current rod moves in REVERSE order
        elif move_count == 2:
            # Even
            if disk_count % 2 == 0:
                current_rod = current_rod_change(current_rod, "+")
            # Odd
            else:
                current_rod = current_rod_change(current_rod, "-")


# The user enters the number of disks on the first(left rod)
diskCount = int(input("Enter the number of initial disks in the first rod: "))
basic_solve(diskCount)
