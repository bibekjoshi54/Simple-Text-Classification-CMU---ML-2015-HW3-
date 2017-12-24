import numpy as np

def XGivenY(XTrain,ytrain):
    yeq1 = ytrain['0'] == 0
    yeq2 = ytrain['0'] == 1
    XTraineq1 = XTrain[yeq1].values
    XTraineq2 = XTrain[yeq2].values
    D = np.array([
        (sum(XTraineq1) + 1)/(2*XTraineq1.shape[0]),
        (sum(XTraineq2) + 1)/(2*XTraineq2.shape[0]),        
    ])
    return D