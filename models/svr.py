from sklearn.svm import SVR
from svmutil import *

def svrtrain(x, y, cost, kernel_select=2):
    prob = svm_problem(y, x)
    param_string = '-s 3 -t {} -c {}'.format(int(kernel_select), int(cost))
    params = svm_parameter(param_string)
    return svm_train(prob, params)

def svrpredict(x, y, model):
    predicted, acc, _ = svm_predict(y, x, model)
    return [predicted, acc]

def svrtrainsk(x, y, cost=1.0, epsilon=0.1):
    model = SVR(C=cost, epsilon=epsilon)
    model.fit(x, y)
    return model

def svrpredictsk(x):
    return model.predict(x)
