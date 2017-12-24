import numpy as np

def XGivenY(XTrain,ytrain):
    yeq1 = ytrain['0'] == 1
    yeq2 = ytrain['0'] == 2
    XTraineq1 = XTrain[yeq1].values
    XTraineq2 = XTrain[yeq2].values
    D = np.array([
        [XTraineq1[:,i].sum() for i in range(XTraineq1.shape[1])],
        [XTraineq2[:,i].sum() for i in range(XTraineq2.shape[1])],        
    ])
    return D
    
