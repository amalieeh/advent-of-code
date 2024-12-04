
list1 = []
list2 = []

with open("day1/input.txt", "r") as file:
    for line in file.readlines():
        list1.append(int(line[:5].strip()))
        list2.append(int(line[8:13].strip()))

file.close()


differeces = []

sortedList1 = list1.sort()
sortedList2 = list2.sort()

for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    differeces.append(diff)

sumDiffereces = sum(differeces)

print(sumDiffereces)


# list1= [3, 4, 2, 1, 3, 3]
# list2= [4, 3, 5, 3, 9, 3]

countOfItemsInList1OccursInList2 = []

for i in range(len(list1)):
    count = list2.count(list1[i])
    countOfItemsInList1OccursInList2.append(count*list1[i])

sumCountOfItemsInList1OccursInList2 = sum(countOfItemsInList1OccursInList2)

print(sumCountOfItemsInList1OccursInList2)


