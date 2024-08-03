import matplotlib.pyplot as plt
import time
def binary_search(arr,key):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            low=mid+1
        else:
            high=mid-1
    return -1

def measure_search_time(num_runs):
    timetaken=[]
    numbers=[]
   
    for _ in range(num_runs):
        n=int(input("enter the number of elements:"))
        arr=list(map(int,input("enter the elements seperated by space: ").split()))
        key=int(input("enter the key element to be searched: "))
        arr.sort()

        start=time.time()
        res=binary_search(arr,key)
        end=time.time()

        totaltime=(end-start)*1000

        timetaken.append(totaltime)
        numbers.append(n)
        if res==-1:
          print(f"the lement is present in the list at position {res} and time it take to find: {totaltime} milliseconds.....! ")
      
        else:
               print("the element is not present in the list!!")
           
    return numbers,timetaken

#ploating
def ploating(number,timetaken):
    plt.plot(number,timetaken,'-o')
    plt.xlabel("number of elements")
    plt.ylabel("time taken in milli seconds")
    plt.grid(True)
    plt.show()


 
n= int(input("enter the number of runs:"))
number,timetaken=measure_search_time(n)
ploating(number,timetaken)
   



    

        

