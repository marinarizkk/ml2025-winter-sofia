# Marina Rizk - ID#308238
# MSCS2202 - Assignment #9.3
# module9_knn_gridsearchcv.py

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Please enter the number of training pairs (positive integers only): "))
    print("\nPlease enter a real number for X and a non-negative integer for Y")
    TrainS = np.empty((N, 2))
    for i in range(N):
        X = float(input(f"Enter X value for training pair #{i+1}: "))
        Y = int(input(f"Enter Y value for training pair #{i+1}: "))
        TrainS[i] = [X, Y]
    X_train = TrainS[:, 0].reshape(-1, 1)
    Y_train = TrainS[:, 1].astype(int)

    M = int(input("\nPlease enter the number of test pairs (positive integers only): "))
    print("\nPlease enter a real number for x and a non-negative integer for y")
    TestS = np.empty((M, 2))
    for i in range(M):
        x = float(input(f"Enter x value for test pair #{i+1}: "))
        y = int(input(f"Enter y value for test pair #{i+1}: "))
        TestS[i] = [x, y]
    x_test = TestS[:, 0].reshape(-1, 1)
    y_test = TestS[:, 1].astype(int)

    max_k = min(10, N)
    optimal = 0.0
    best_ks = []
    for k in range(1, max_k + 1):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        y_pred = model.predict(x_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"\nk = {k}, Test Accuracy = {acc:.4f}")
        if acc > optimal:
            optimal = acc
            best_ks = [k]
        elif acc == optimal:
            best_ks.append(k)
    print(f"\nBest k value(s): {best_ks}")
    print(f"Best test accuracy: {optimal:.4f}")

if __name__ == "__main__":
    main()
