import random as rand
dice = 0
lst = [0, 0, 0, 0, 0, 0]
for _ in range(100):
    dice = rand.randint(1,6)
    if(dice == 1):
        lst[0] = lst[0] + 1
    elif(dice == 2):
        lst[1] = lst[1] + 1
    elif(dice == 3):
        lst[2] = lst[2] + 1
    elif(dice == 4):
        lst[3] = lst[3] + 1
    elif(dice == 5):
        lst[4] = lst[4] + 1
    elif(dice == 6):
        lst[5] = lst[5] + 1
print("1 =>", lst[0])
print("2 =>", lst[1])
print("3 =>", lst[2])
print("4 =>", lst[3])
print("5 =>", lst[4])
print("6 =>", lst[5])