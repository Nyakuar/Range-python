x = range(20)
for y in x:
    if y%x:
        if y%2 ==0:
            print(f"{y}divisible 2")
        elif y%3==0:
            print(f"{y}divisible 3")
            
        else:
            print(f"{y}divisible 2 or 3")