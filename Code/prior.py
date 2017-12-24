

def prior(y,val = 1):
    return y[y['0'] == val].shape[0]/y.shape[0]