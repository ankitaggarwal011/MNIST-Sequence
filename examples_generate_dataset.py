from mnist_sequence_api import MNIST_Sequence_API

api_object = MNIST_Sequence_API()

seq_len = 5 # generate sequences of this length
n_train = 50
inputs, labels = api_object.generate_data(n_train, seq_len)
api_object.save_array(inputs, "dataset/train_inputs.bc")
api_object.save_array(labels, "dataset/train_labels.bc")

n_validation = 25
inputs, labels = api_object.generate_data(n_validation, seq_len)
api_object.save_array(inputs, "dataset/test_inputs.bc")
api_object.save_array(labels, "dataset/test_labels.bc")