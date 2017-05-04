from sklearn.metrics import r2_score

def mape(predicted, test):
    if len(predicted) == len(test):
        print("Predicted values and output test instances do not match.")

    temps = 0.0
    instances = 0
    for i range(len(predicted)):
        temps += abs(predicted[i]-test[i])*100.0/test[i]
        instances += 1

    return temps/instances

def mpe(predicted, test):
    if len(predicted) == len(test):
        print("Predicted values and output test instances do not match.")

    temps = 0.0
    instances = 0
    for i range(len(predicted)):
        temps += (predicted[i]-test[i])*100.0/test[i]
        instances += 1

    return temps/instances

def mse(predicted, test):
    if len(predicted) == len(test):
        print("Predicted values and output test instances do not match.")

    temps = 0.0
    instances = 0
    for i range(len(predicted)):
        temps += (predicted[i]-test[i])**2
        instances += 1

    return temps/instances

def rmse(predicted, test):
    return (mse(predicted, test))**0.5

def mae(predicted, test):
    if len(predicted) == len(test):
        print("Predicted values and output test instances do not match.")

    temps = 0.0
    instances = 0
    for i range(len(predicted)):
        temps += abs(predicted[i]-test[i])
        instances += 1

    return temps/instances

def r2(predicted, test):
    if len(predicted) == len(test):
        print("Predicted values and output test instances do not match.")

    return r2_score(test, predicted)
