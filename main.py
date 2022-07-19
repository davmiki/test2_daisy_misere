import numpy as np
from turtle import Screen
screen = Screen()
#list1 = [10,8,]
answer = (screen.textinput("Daisy TEST", "Enter list of numbers with space seperation"))
print(answer)
#Input list to examine
lis_to_exam= [int(x) for x in answer.split()]
#lisss= lis_to_exam.copy()
print(f"lis_to_exam in main = {lis_to_exam}")
# lis_canon = to_canonic(lis_to_exam)
lis_canon = lis_to_exam
print(f"lis_canon = {lis_canon}")
list1 = lis_canon
#list_long = calc_list_long_list1(list1)
print("list1 ",list1)
print("len(list1) =  ",len(list1))

mt =np.array([[0, 1, 2, 3],
         [1, 0, 3, 2],
         [2, 3, 0, 1],
         [3, 2, 1, 0]])


def nhe(number):
    if number==0:
        return 0
    elif number % 2 == 0:
        return 2
    else :
        return 1

def wet (number):
    if number == 1 or number == 3 or number == 0:
        return 0
    elif number ==2 :
        return 1
    else :
        return number - 3

def weight (list):
    wete = 0
    for num in list:
        # print(f"num = {num}  ,  wet(num)= {wet(num)}")
        wete += wet(num)
    return wete


def is_pn(list):
    nwd = [num_heap_equ(list), weight(list), deficit(list)]
    if num_heap_equ(list)==0:
        if weight(list) == 0:
           npan= [True,1]
           return npan
        elif weight(list) == 2:
            if deficit(list) == 2:
                npan = [True, 2]
                return npan
            else:
                return [False,nwd]
        elif deficit(list) >=4:
           npan = [True, 3]
           return npan
        else:
            nwd = [num_heap_equ(list), weight(list), deficit(list)]
            npan = [False, nwd]
            return npan
    else:
         nwd = [num_heap_equ(list),weight(list) ,deficit(list)]
         npan = [False,nwd]
         return npan

def is_np(list):
    nwd = [num_heap_equ(list), weight(list), deficit(list)]
    if num_heap_equ(list) == 1:
        if weight(list) == 0:
           return [True,4]
        else:
            return [False, nwd]
    elif num_heap_equ(list) == 3:
        if deficit(list) >= 5:
           return [True,5]
        else:
            return [False, nwd]
    else:
        return [False, nwd]


def deficit (list):
    defi = 0
    for num in list:
        # print(f"num = {num}  ,  wet(num)= {wet(num)}")
        defi  +=  wet(num)
        # print(f"deficit of num = {defi}")
    mw = wet(max(list))
    # print(f"mw - {mw}")
    return mw*2 -defi

def num_heap_equ(list):
    nhud = nhe(list[0])
    for i in range(len(list)):
        if i < len(list)-1:
            # print(f"i = {i}, nhud = {nhud} , nhe(i+1) = {nhe(i+1)}")
            nhud = mt[nhud][nhe(list[i+1])]
    return nhud


mx= max(list1)
print("max of list = ",mx)
print(f"  list1 = {list1}")
print(f"len of list1 = {len(list1)}")
print(f"weight of list1 = {weight(list1)}")
print(f"deficit  of list1 = {deficit(list1)}")
print(f"num_heap_equ  of list1 = {num_heap_equ(list1)}")
res = is_pn(list1)
print(f"is_pn  of list1 = num_heap_equ,  weight, deficit {res}")
res1 = is_np(list1)
print(f"is_np  of list1 = num_heap_equ,  weight, deficit {res1}")

mt =np.array([[3, 2, 1, 0],
         [2, 3, 0, 1],
         [1, 0, 3, 2],
         [0, 1, 2, 3]])

