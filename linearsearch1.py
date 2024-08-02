import time
import matplotlib.pyplot as plt

# Linear search function
def linear_search(n,arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def measure_search_time(num_runs):
    nforplot=[]
    time_taken=[]
    for i in range(num_runs):
        n=int(input("Enter the number of elements: "))
        arr=list(map(int,input("enter elements of array: ").split()))
        key=int(input("enter the key element to be searched: "))
        start=time.time()
        res=linear_search(n,arr,key)
        end=time.time()
        totaltime=(end-start)*100# converting into milli seconds
        nforplot.append((n))
        time_taken.append(totaltime)
        if res==-1:
            print("the element is not found in the array!!")
        else:
            print(f"the element is found at position {res} in the array!!")
            print(f"total time it took {totaltime} milliseconds to find the element...!")
    return nforplot,time_taken
            


#ploting
def ploting(nforplot,time_taken):
    
    plt.plot(nforplot, time_taken, 'o-')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time Taken (milliseconds)')
    plt.title('Linear Search Time Complexity')
    plt.grid(True)
    plt.show()


# Main execution
if __name__ == "__main__":
    num_runs = int(input("Enter the number of runs: "))
    results,time_taken = measure_search_time(num_runs)
    ploting(results,time_taken)
