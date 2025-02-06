value = int(input("Enter a value:"))

for i in range(1, value+1):
    counter = i
    flag = True
    for j in range(1, value+1):
        if i > (value + 1) / 2:
            i = value + 1 - i
            counter = i
        print(counter, end =" ")
        if j == (value+1)/2:
            flag = False
        if flag:
            counter +=1
        else:
            counter -=1
    print()
