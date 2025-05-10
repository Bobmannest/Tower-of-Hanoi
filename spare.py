#Checks if other rods are empty so an error does not occur
def left_rod_check(rods, current_rod):
    if not len(rods[(current_rod+1) % 3]):
        return 0
    else:
        return len(rods[(current_rod+1) % 3][-1])

def right_rod_check(rods, current_rod):
    if not len(rods[(current_rod+1) % 3]):
        return 0
    else:
        return len(rods[(current_rod-1) % 3][-1])