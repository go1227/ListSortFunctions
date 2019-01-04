__author__ = "Guilherme Ortiz"
__version__ = "1.0"
__date_last_modification__ = "1/3/2018"
__python_version__ = "1"

#Compilation of sorting algorithms and demonstration on which one is more effective for a random list of numbrers

import time
import random

valid_input = False
listsize = 0
print("\nThis program will demonstrate which list sorting method is the most efficient using a random list of numbers.")
while valid_input is False:
    listsize = input("Please enter the number of elements you would like to have in your list [100-50000]:\n")
    if listsize.isdigit() and int(listsize)>=100 and int(listsize)<=50000:
        valid_input = True


#Insert Sort:
def insertSort(mylist):
    for index in range(1, len(mylist)):
        currentval = mylist[index]
        pos = index

        while pos > 0 and mylist[pos-1] > currentval:
            mylist[pos] = mylist[pos-1]
            pos = pos - 1
        mylist[pos] = currentval


#Bubble Sort:
def bubbleSort(mylist):
    for index in range(len(mylist)-1,0,-1):
        for i in range(index):
            if mylist[i] >  mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp


#Selection Sort:
def selectionSort(mylist):
    for fillslot in range(len(mylist)):
        posOfMaxElement = 0
        for location in range(1, fillslot+1):
            if mylist[location] > mylist[posOfMaxElement]:
                posOfMaxElement = location
        tmp = mylist[fillslot]
        mylist[fillslot] = mylist[posOfMaxElement]
        mylist[posOfMaxElement] = tmp

#Shell Sort
def shellSort(mylist):
    sublistcount = len(mylist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(mylist, startposition, sublistcount)
        #print("After increments of size", sublistcount, "The list is", mylist)
        sublistcount = sublistcount // 2

def gapInsertionSort(mylist, start, gap):
    for i in range(start + gap, len(mylist), gap):
        currentvalue = mylist[i]
        position = i
        while position >= gap and mylist[position - gap] > currentvalue:
            mylist[position] = mylist[position - gap]
            position = position - gap
        mylist[position] = currentvalue


#Merge Sort
def mergeSort(mylist):
    #print("Splitting ",mylist)
    if len(mylist)>1:
        mid = len(mylist)//2
        lefthalf = mylist[:mid]
        righthalf = mylist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                mylist[k]=lefthalf[i]
                i=i+1
            else:
                mylist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            mylist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            mylist[k]=righthalf[j]
            j=j+1
            k=k+1


#Quick Sort
def quickSort(mylist):
   quickSortHelper(mylist,0,len(mylist)-1)
def quickSortHelper(mylist,first,last):
   if first<last:
       splitpoint = partition(mylist,first,last)
       quickSortHelper(mylist,first,splitpoint-1)
       quickSortHelper(mylist,splitpoint+1,last)
def partition(mylist,first,last):
   pivotvalue = mylist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and mylist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while mylist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = mylist[leftmark]
           mylist[leftmark] = mylist[rightmark]
           mylist[rightmark] = temp
   temp = mylist[first]
   mylist[first] = mylist[rightmark]
   mylist[rightmark] = temp

   return rightmark


tmp = list(range(1, int(listsize)))
random.shuffle(tmp)
testlist1 = tmp.copy()
testlist2 = tmp.copy()
testlist3 = tmp.copy()
testlist4 = tmp.copy()
testlist6 = tmp.copy()
testlist7 = tmp.copy()
testlist5 = tmp.copy()


start_time = time.time()
insertSort(testlist1)
print('\nInsertSort() --- Execution time: %s seconds' % (time.time() - start_time))

start_time = time.time()
bubbleSort(testlist2)
print('\nBubbleSort() --- Execution time: %s seconds' % (time.time() - start_time))

start_time = time.time()
selectionSort(testlist3)
print('\nSelectionSort() --- Execution time: %s seconds' % (time.time() - start_time))

start_time = time.time()
shellSort(testlist4)
print('\nShellSort() --- Execution time: %s seconds' % (time.time() - start_time))

start_time = time.time()
mergeSort(testlist6)
print('\nMergesSort() --- Execution time: %s seconds' % (time.time() - start_time))

start_time = time.time()
quickSort(testlist7)
print('\nQuickSort() --- Execution time: %s seconds' % (time.time() - start_time))

start_time = time.time()
testlist5.sort()
print('\nlist.sort() (python built-in function) --- Execution time: %s seconds' % (time.time() - start_time))