# Marina Rizk - ID#308238
# MSCS2202 - Assignment #4.2

def ListCheck():
    N = int(input("Please enter the number of elements in your list (positive integers only): "))

    if N <= 0:
        print("Please enter a positive integer")
        ListCheck()

    else:
        inputs = []
        for i in range(1, N+1):
            x = int(input("Please enter element {} in your list: ".format(i)))
            inputs.append(x)

        y = int(input("Please enter the integer to find its position in the list: "))
        if y in inputs :
            print(inputs.index(y) + 1)
        else:
            print("-1")

ListCheck()
