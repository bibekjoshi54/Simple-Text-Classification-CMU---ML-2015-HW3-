import scipy.io
import pandas as pd

def genCSV():
    hw3Data = scipy.io.loadmat('../hw3/HW3Data.mat')
    keys = [i for i in hw3Data.keys() if '_' not in i]
    data = {}
    for k in keys:
        try:
            tempData = hw3Data[k]
            tempData = tempData.todense()
            data[k] = tempData
        except AttributeError:
            data[k] = hw3Data[k]
    for i in data:
        print('Generating ' + i + '.csv')
        pd.DataFrame(data[i]).to_csv('../Data/'+i+'.csv')

genCSV()