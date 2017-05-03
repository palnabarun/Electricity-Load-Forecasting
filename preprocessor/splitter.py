def split_train_test(dataset, trainr=0.8, valr=0.0, testr=0.2):
    train_input = []
    train_output = []
    val_input = []
    val_output = []
    test_input = []
    test_output = []

    for instance in dataset:
        input_data += dataset[0]
        output_data += dataset[1]

    split1 = int(len(dataset)*trainr)
    split2 = int(len(dataset)*(trainr+valr))

    train_input = input_data[:split1]
    train_output = output_data[:split1]

    val_input = input_data[split1:split2]
    val_output = output_data[split1:split2]

    test_input = input_data[split2:]
    test_output = output_data[split2:]

    return [train_input, train_output, val_input, val_output, test_input, test_output]
