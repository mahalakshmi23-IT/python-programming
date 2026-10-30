#Print Array Elements
n=input()
arr=input()
print(arr,sep=" ")
#Sum of Array Elements
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))
#Sum of Odd and Even Elements in an Array
n = int(input())
arr = list(map(int, input().split()))

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(even, odd)

#Sum of Elements at Odd and Even Indices in an Array
n=int(input())
arr=list(map(int, input().split()))
even=0
odd=0
for i in range(n):
    if i%2==0:
        even+=arr[i]
    else:
        odd+=arr[i]
print(even, odd)

#Find Maximum Element in an Array
n=input()
arr = list(map(int, input().split()))
print(max(arr))

#Find Minimum Element in an Array
n=input()
arr = list(map(int, input().split()))
print(min(arr))
#Find Maximum Odd and Even Elements in an Array

import sys
size=int(input())
arr = list(map(int, input().split()))
emax=omax=-sys.maxsize-1
for i in arr:
  if i%2==0:
    if i>emax:
      emax=i
  else:
    if i>omax:
      omax=i
if emax==-sys.maxsize-1:
  print("None")
else:
  print(emax)
if omax==-sys.maxsize-1:
  print("None")
else:
  print(omax)

#Check if a Key Number Exists in an Array

n=input()
arr = list(map(int, input().split()))
key=int(input())
if key in arr:
  print("Yes")
else:
  print("No")

#find Index of a Key Number in an Array
n = int(input())
s = list(map(int, input().split()))
key = int(input())
if key in s:
    print(s.index(key))
else:
    print(-1)

