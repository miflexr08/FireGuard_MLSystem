from data_sets import *
from neural_net import *

# Test it in a function format (function aproximation concept)
weights = [
    #toes wlrec nfans
    [0.1, 0.1, -0.3], #hurt
    [0.1, 0.2, 0.0], #win
    [0.0, 1.3, 0.1] #sad
]

input_data = [toes[0], wlrec[0], nfans[0]]

neural_net = NeuralNetwork(input_data, weights)

# 1. Run prediction with current weights
neural_net.run_prediction()
print("current prediction: "+neural_net.current_prediction)

# 2. Calculate error and delta (gradient)
neural_net.calculate_error(real_data=[hurt[0], win[0], sad[0]])
print("current error: "+neural_net.current_error)

print("current weights: "+ neural_net.weights)
# 3. Adjust the weights
neural_net.gradient_descent()






















def w_sum(vect, matrix):
    pass