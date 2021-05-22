#USING BUBBLE SORT
lst=eval(input("Enter a list of numbers: "))

#ascending sort
for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
    else:
        pass

print("Sorting in ascending order using Bubble sort: ",lst)

#descending sort
for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j]<lst[j+1]:
            b=lst[j],lst[j+1]=lst[j+1],lst[j]
    else:
        pass

print("Sorting in descending order using Bubble sort: ",lst)

print()

#USING INSERTION SORT
lst=eval(input("Enter a list of numbers: "))

#ascending sort
for i in range(1,len(lst)):
    current=lst[i]
    pos=i
    while current<lst[pos-1] and pos>0:
        lst[pos]=lst[pos-1]
        pos=pos-1
    else:
        lst[pos]=current

print("Sorting in ascending order using Insertion sort: ",lst)

#descending sort
for i in range(1,len(lst)):
    current=lst[i]
    pos=i
    while current>lst[pos-1] and pos>0:
        lst[pos]=lst[pos-1]
        pos=pos-1
    else:
        lst[pos]=current

print("Sorting in descending order using Insertion sort: ",lst)




