#Even num of disks = left option, Odd num of disks= right option
def odd_or_even(current_rod, rods):
    if len(rods[current_rod]) % 2 == 0:
        print("even")
        # Pops items depending on the current rod
        if current_rod == 0:
            item_to_move = rods[0].pop()
            rods[1].append(item_to_move)
        elif current_rod == 1:
            item_to_move = rods[1].pop()
            rods[0].append(item_to_move)
        elif current_rod == 2:
            item_to_move = rods[2].pop()
            rods[0].append(item_to_move)
    else:
        print("odd")
        # Pops items depending on the current rod
        if current_rod == 0:
            item_to_move = rods[0].pop()
            rods[2].append(item_to_move)
        elif current_rod == 1:
            item_to_move = rods[1].pop()
            rods[2].append(item_to_move)
        elif current_rod == 2:
            item_to_move = rods[2].pop()
            rods[1].append(item_to_move)

#Solves a new game of Tower of Hanoi
def basic_solve(disk_count):
    move_count = pow(2, disk_count) - 1
    current_rod = 0
    rods = [[],[],[]]
    #Builds starting layout
    for _ in range(disk_count):
        rods[0].append(disk_count)
        disk_count -= 1

    #Repeats 2 to the power of the number of disks - 1
    for _ in range(move_count):
        print("\n",rods[0],"\n",rods[1],"\n",rods[2],"\n")
        odd_or_even(current_rod, rods)

#The user chooses whether to fully complete a new game or finish an already started one
decide = 0
while decide != 1 and decide != 2:
    decide = int(input("1 - Basic solve \n2 - Finish solving\nEnter:"))

if decide == 1:
    diskCount = int(input("Enter the number of starting disks in the first rod: "))
    basic_solve(diskCount)
elif decide == 2:
    print(int(input("Custom")))

