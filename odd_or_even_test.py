def odd_or_even(current_rod, rods):
    print(current_rod)
    if len(rods[current_rod]) % 2 == 0:
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

#When current rod is 3 and needs to be +1, it should go back to rod 1 and vice versa
def current_rod_change(current_rod, decision):
    if decision == "+":
        current_rod += 1
    elif decision == "-":
        current_rod -= 1

    #Makes sure current_rod value doesn't go over 2 and under 0
    if current_rod < 0:
        current_rod = 2
    elif current_rod > 2:
        current_rod = 0
    return current_rod

#Main
current_rod = 0
rods = [[3,2,1],[],[]]

odd_or_even(current_rod, rods)
odd_or_even(current_rod, rods)
current_rod = current_rod_change(current_rod, "-")
odd_or_even(current_rod, rods)
current_rod = current_rod_change(current_rod, "+")
odd_or_even(current_rod, rods)
current_rod = current_rod_change(current_rod, "+")
odd_or_even(current_rod, rods)
odd_or_even(current_rod, rods)
current_rod = current_rod_change(current_rod, "-")
odd_or_even(current_rod, rods)
current_rod = current_rod_change(current_rod, "+")

print("\n",rods[0],"\n",rods[1],"\n",rods[2],"\n")