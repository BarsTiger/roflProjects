import random, time
import datetime

try:
    n = int(input("How many numbers you want to sort: "))
except:
    print("Not int...")
    n = random.randint(10, 1000)
print("I will generate " + str(n) + " numbers")

type = input("Which type of sorting do you want?\n"
             "1 - My proprietary algorithm\n"
             "2 - Python original sorted() algorithm\n"
             "Type here: ")

list = []
for i in range(n * 2):
    list.append(random.randint(1, 10000))

def ultrasort(list):
    sortedlist = []
    for j in list:
        minimal = list[0]
        for i in list:
            if i < minimal:
                minimal = i
        sortedlist.append(minimal)
        list.remove(minimal)
    return sortedlist

timestart = time.time_ns()
if type == "1":
    print(ultrasort(list))
else:
    print(sorted(list))
elapsed = time.time_ns() - timestart
elapsed = elapsed / 1000000000
print(str(datetime.timedelta(seconds=elapsed)))

input()
