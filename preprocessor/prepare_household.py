import numpy as np
import time
import csv
import os

source = "..\\dataset\\household_power_consumption.txt"

def consume_data():
    with open(source) as f:
        data = csv.reader(f, delimiter=";")
        dataset = []
        instances = 0
        for line in data:
            try:
                dataset.append(float(line[2]))
                instances += 1
            except ValueError:
                dataset.append(0.0)
                instances += 1

    return [dataset, instances]

def subsample_data(dataset, group_into=1):
    ret_data = []
    ret_instances = 0
    temps = 0.0
    it = 0
    for value in dataset:
        temps += value
        it += 1
        if it == group_into:
            ret_data.append(temps)
            ret_instances += 1
            temps = 0.0
            it = 0
    return [ret_data, ret_instances]

def prepare_data(dataset, look_back=50):
    ret_data = []
    instances = 0
    for i in range(len(dataset[look_back:])):
        ret_data.append(dataset[i:i+look_back])
        ret_data.append(dataset[i+look_back])
        instances += 1
    return [ret_data, instances]
