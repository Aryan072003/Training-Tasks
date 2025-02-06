import json

f = open("text.txt", "r")
stack = json.loads(f.read())

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

with open("text.txt", "w") as file:
    file.write(json.dumps(stack))
    file.close()

