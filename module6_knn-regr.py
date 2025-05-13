# Marina Rizk - ID#308238
# MSCS2202 - Assignment #6.2
# module6_knn-regr.py

import numpy as np

class knn_regr:
    def __init__(self,k):
        self.k = k
        self.pairs = np.empty((0,2))
        
    def ListAppend(self, x, y):
        self.pairs = np.vstack((self.pairs, np.array([[x, y]])))

    def K_NN(self, x_query):
        Manhattan_Distance = np.abs(self.pairs[:, 0] - x_query) 
        nneighbor = np.argsort(Manhattan_Distance)[:self.k]
        npredict = self.pairs[nneighbor, 1]
        return np.mean(npredict)
            
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Please enter the number of points in your list (positive integers only): "))
            if(N > 0):
                break
            else:
                print("Please enter a positive integer")

        except ValueError:
            print("Please enter a positive integer")

    while True:
        try:
            k = int(input("Please enter the k-factor for k-NN regression (positive integers <= N only): "))
            if(k > 0 and k <= N):
                break
            elif (k > N):
                print("Please enter a positive integer that is smaller than or equal N.")
            else:
                print("Please enter a positive integer")

        except ValueError:
            print("Please enter a positive integer")
    Regr_Inst = knn_regr(k)


    for i in range(1, N+1):
        while True:
            try:
                x = float(input("Please enter X{} in your list: ".format(i)))
                y = float(input("Please enter Y{} in your list: ".format(i)))
                Regr_Inst.ListAppend(x,y)
                break
                
            except ValueError:
                print("Please enter a numeric value")


while True:
    try:
        x_predict = float(input("Please enter X value to find the result of its k-NN Regression: "))
        print(Regr_Inst.K_NN(x_predict))
        break
        
    except ValueError:
        print("Please enter a numeric value")
