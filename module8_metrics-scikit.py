# Marina Rizk - ID#308238
# MSCS2202 - Assignment #8.2
# module8_metrics-scikit.py

import numpy as np
from sklearn.metrics import precision_score, recall_score

def program():
    while True:
        try:
            N = int(input("Please enter the number of points in your list (positive integers only): "))
            if(N > 0):
                break
            else:
                print("Please enter a positive integer")

        except ValueError:
            print("Please enter a positive integer")

    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    for i in range(N):
      while True:
            try:
                x = int(input(f"Please enter ground truth X{i+1}: "))
                if x in (0, 1):
                    X[i] = x
                    break
                else:
                    print("Value must be either 0 or 1")
            except ValueError:
                print("Value must be either 0 or 1")

      while True:
            try:
                y = int(input(f"Please enter predicted Y{i+1}: "))
                if y in (0, 1):
                    Y[i] = y
                    break
                else:
                    print("Value must be either 0 or 1")
            except ValueError:
                print("Value must be either 0 or 1")
                
    print(f"\nPrecision = {precision_score(X, Y): .2f}")
    print(f"Recall = {recall_score(X, Y): .2f}")

if __name__ == "__main__":
  program()
