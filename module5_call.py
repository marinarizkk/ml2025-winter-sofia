# Marina Rizk - ID#308238
# MSCS2202 - Assignment #5.2
# module5_call.py

from module5_mod import ListReader
            
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Please enter the number of elements in your list (positive integers only): "))
            if(N > 0):
                break
            else:
                print("Please enter a positive integer")

        except ValueError:
            print("Please enter a positive integer")

    ListCase = ListReader()


    for i in range(1, N+1):
        while True:
            try:
                x = int(input("Please enter element {} in your list: ".format(i)))
                ListCase.ListAppend(x)
                break

            except ValueError:
                print("Please enter an integer value")



    y = int(input("Please enter a number to find its position in the list: "))
    print(ListCase.InputPos(y))
