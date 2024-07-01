# to find the largest sum of subarray of contiguos elements
list = []
countlist =[]
subarray = []
count = 0
sum =0
n = int(input("Enter the size:"))
for i in range (0,n):
    element=int(input("enter the element"))
    list.append(element)
    if element>=0:
        countlist.append(i)
start = countlist[0]
end = countlist[-1]
for i in range (start,end+1):
    e=list[i]
    subarray.append(e)
    sum=sum+list[i]
print(f'The subarray is {subarray} and sum is {sum}')
