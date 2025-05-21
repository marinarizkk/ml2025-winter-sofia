# Marina Rizk - ID#308238
# MSCS2202 - Assignment #7.2
# module7_knn-regr-scikit.py

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class Train_Data:
    pairs_x = []
    pairs_y = []
    pairs = None
    
    def __init__(self,k):
        self.k = k
        
    def ListAppend(self, x, y):
        Train_Data.pairs_x.append(x)
        Train_Data.pairs_y.append(y)

    def K_NN(self, x_query):
        KNN_X = np.array(Train_Data.pairs_x).reshape(-1, 1)
        KNN_Y = np.array(Train_Data.pairs_y)
        knn_regressor = KNeighborsRegressor(n_neighbors=k)
        knn_regressor.fit(KNN_X, KNN_Y)
        y_prediction = knn_regressor.predict(np.array([[x_predict]]))
        print(y_prediction[0])
            
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
    Regr_Inst = Train_Data(k)


    for i in range(1, N+1):
        while True:
            try:
                x = float(input("Please enter X{} in your list: ".format(i)))
                y = float(input("Please enter Y{} in your list: ".format(i)))
                Regr_Inst.ListAppend(x,y)
                break
                
            except ValueError:
                print("Please enter a numeric value")
        
        Train_Data.pairs = np.column_stack((Train_Data.pairs_x, Train_Data.pairs_y))
    print("\nThe variance of labels in the training dataset is ", np.var(Train_Data.pairs_y), "\n")


    while True:
        try:
            x_predict = float(input("Please enter X value to find the result of its k-NN Regression: "))
            break
            
        except ValueError:
            print("Please enter a numeric value")
    Regr_Inst.K_NN(x_predict)
