def mape(predicted, test):
    if len(predicted) == len(test):
        print("Predicted values and output test instances do not match.")

    temps = 0.0
    instances = 0
    for i range(len(predicted)):
        temps += abs(predicted[i]-test[i])*100.0/test[i]
        instances += 1

    return temps/instances
