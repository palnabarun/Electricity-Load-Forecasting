from svmutil import *

def svrtrain(x, y, cost, kernel_select=2):
    prob = svm_problem(y, x)
    param_string = '-s 3 -t {} -c {}'.format(int(kernel_select), int(cost))
    params = svm_parameter(param_string)
    return svm_train(prob, params)

def svrpredict(x, y, model):
    predicted, acc, _ = svm_predict(y, x, model)
    return [predicted, acc]
