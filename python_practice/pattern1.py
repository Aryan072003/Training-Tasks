while True:
    rows = int(input("Enter the rows of cell:"))
    cols = int(input("Enter the columns of cell:"))

    if rows != 0 and cols != 0:
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                print(f"{j + cols * (i - 1)} ", end=" ")
            print()
    else:
        print("Exit")
        break
