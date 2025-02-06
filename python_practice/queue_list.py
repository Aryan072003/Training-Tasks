queue = [1,2,3,4,5,6]

def queue_push(lst,x):
    lst.append(x)
    return lst
def queue_pop(lst):
    lst = lst[1:]
    return lst

while True:
    a = int(input("Enter a choice:"))

    if a == 1:
        b = int(input("Enter a number to push:"))
        print(queue_push(queue, b))
    elif a == 2:
        print(queue_pop(queue))
    elif a == 0:
        print("Exit")
        break