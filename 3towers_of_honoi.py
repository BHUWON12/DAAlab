

def toh(n,a,b,c):
    global count
    if n>0:
        toh(n-1,a,c,b)
        print(f"disk {n} {a}->{c}")
        count+=1
        toh(n-1,b,a,c)


#main part
source='Source'
temp='Temp'
dest='Dest'
count=0
n=int(input("Enter the number of disks:"))
print("Sequence is:")
toh(n,source,temp,dest)
print("The number of Moves:",count)