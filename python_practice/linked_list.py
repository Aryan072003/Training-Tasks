dict = {
    "a": {"data": "abc", "next": "b"},
    "b": {"data": "def", "next": "c"},
    "c": {"data": "ghi", "next": "d"},
}

while True:
    a = int(input("Enter a choice:"))

    if a == 1:
        key = input("Enter the address:")
        data = input("Enter the data:")
        next = input("Enter next address:")

        if key in dict.keys():
            print("Element exists")
            continue

        if (key and next) not in dict.keys():
                print("Enter valid next element")
        else:
                dict.update({key: {"data": data, "next": next}})
                print(dict)

    elif a == 2:
        key = input("Enter the address:")

        if key in dict.keys():
            dict.pop(key)
            print(dict)
        else:
            print("Enter valid element to remove")
    elif a == 0:
        print("Exit")
        break



