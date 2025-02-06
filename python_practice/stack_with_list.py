stack = [1,2,3,4,5,6]

def stack_push(lst,x):
    lst.append(x)
    return lst
def stack_pop(lst):
    lst.pop()
    return lst

while True:
    a = int(input("Enter a choice:"))
    if a == 1:
        b = int(input("Enter a number to push:"))
        print(stack_push(stack, b))
    elif a == 2:
        print(stack_pop(stack))
    elif a == 0:
        print("Exit")
        break