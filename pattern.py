#square pattern
n=4
for row in range(1,n+1):
  print("*"*5)
#right angle triangle
n=5
for row in range(1,n+1):
  print("*"*row)

#using num
n=5
for row in range(1,n+1):
  for col in range(1,row+1):
    print(col,end="")
  print()  

#num 
n=5
for row in range(1,n+1):
  print(str(row)*row)
#number

n=5
num=1
for row in range(1,n+1):
  for col in range(1,row+1):
    print(num,end=" ")
    num+=1
  print()  


