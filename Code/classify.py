import numpy as np
import logProd
import pandas as pd

def classify(EstProb,p,Xtest):
    '''
    Beta is Assumed to be (2,1)
    '''
    testSize = Xtest.shape[0]
    yhat = np.zeros(testSize,dtype=int)
    Xtest = Xtest.values
    for i in range(testSize):
        thetaechno = EstProb[0] * Xtest[i] + (1-EstProb[0]) * (1-Xtest[i])
        thetaonion = EstProb[1] * Xtest[i] + (1-EstProb[1]) * (1-Xtest[i])
        echnoScore = logProd.logProd(np.array([np.log(p), np.log(thetaechno).sum()]))
        onionScore = logProd.logProd(np.array([np.log(1-p),np.log(thetaonion).sum()]))    
        if onionScore > echnoScore:
            yhat[i] = 1
    return pd.DataFrame(yhat.reshape(-1,1))
