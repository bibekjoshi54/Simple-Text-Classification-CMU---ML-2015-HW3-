import genCSV
import classify
import xGivenY
import prior
import ClassificationError
import pandas as pd

def main():
    genCSV.genCSV()
    print('Reading Required Files')
    XTrain = pd.read_csv('../Data/XTrain.csv')
    yTrain = pd.read_csv('../Data/yTrain.csv') - 1
    XTest = pd.read_csv('../Data/XTest.csv')
    yTest = pd.read_csv('../Data/yTest.csv') - 1
    print('Calculating Prior')
    p = prior.prior(yTrain)
    print('Calculating Estimated Probailites')
    estProb = xGivenY.XGivenY(XTrain, yTrain)
    print('Classifying')
    yhatTrain = classify.classify(estProb, p, XTrain)
    print(ClassificationError.classificationError(yhatTrain.values, yTrain.values))
    print('Classifying the Test')
    yhatTest = classify.classify(estProb, p, XTest)
    print(ClassificationError.classificationError(yhatTest.values, yTest.values))


main()