x = range(1,20,5)
for a  in x: 
    print(a)
    
    x = range(10)
for b  in x: 
    print(b)
    x = range(6)
for n in x:
     print(n)
     
x = range(3, 20, 2)
for n in x:
  print(n)

for i in range(10):
    print(i, end=" ")
print()
 
# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print()
 
# performing sum of natural
# number
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)