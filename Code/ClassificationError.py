def classificationError(yhat, ytrue):
    '''
    yhat : It Must Be Dataframe (n *1)
    ytrue: It must be Data frame (n *1)
    return: Return the error rate
    '''
    return (yhat != ytrue).sum()/len(yhat)