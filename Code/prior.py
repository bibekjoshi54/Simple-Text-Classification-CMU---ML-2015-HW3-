

def prior(y):
    return y[y['0'] == 0].shape[0]/y.shape[0]