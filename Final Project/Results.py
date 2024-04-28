from tabulate import tabulate

print(tabulate([[15,10,10,20,2],[15,10,10,50,2],[15,5,10,20,2],['1-15',10,10,15,2]], headers=['UserId', 'NN Param','Num_Rec','Iterations','MAE'], numalign= 'None'))