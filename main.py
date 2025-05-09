#Solves a brand new game of Tower of Hanoi
def basicSolve(diskCount):
    rod1 = []
    rod2 = []
    rod3 = []
    for _ in range(diskCount):
        rod1.append(diskCount)
        diskCount -= 1
    print(rod1)

#The user chooses whether to fully complete a new game or finish an already started one
decide = 0
while decide != 1 and decide != 2:
    decide = int(input("1 - Basic solve \n2 - Finish solving\nEnter:"))

if decide == 1:
    diskCount = int(input("Enter the number of starting disks in the first rod: "))
    basicSolve(diskCount)
elif decide == 2:
    print(int(input("Custom")))

