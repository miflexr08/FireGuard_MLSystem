from data_sets import *
from neural_net import *

# Test it in a function format (function approximation concept)
weights = [
    #toes #wlrec #nfans
    [0.1, 0.1, -0.3], #hurt
    [0.1, 0.2, 0.0], #win
    [0.0, 1.3, 0.1] #sad
]
input_data = [toes[0], wlrec[0], nfans[0]]
neural_net = NeuralNetwork(input_data, weights)

# Notes:
# 1. Move it inside the NeuralNetwork class
# 2. Each prediction can have it's own LIMIAR_ERROR
# 3. What about comparing the sum's of limiar errors
# to the individual prediction errors (when data is tighly related)
# Desta forma eu teria algo como erros individuais e um limiar de erro geral,
# podendo calcular desvio médio padrão por feature (?)
# Qual é o problema em comparar o limiar de erro com o erro quadrado médio?
# Tomar nota das propriedades escondidas na multiplicação do input pelo erro
while True:

    # 1. Run prediction with current weights
    neural_net.run_prediction()
    print("current prediction: "+neural_net.current_prediction)

    if neural_net.converged():
        break

    # 2. Calculate error and delta (gradient)
    delta_error = neural_net.calculate_error(real_data=[hurt[0], win[0], sad[0]])
    print("current error: "+neural_net.current_error)

    print("current weights: "+ neural_net.weights)
    # 3. Adjust the weights
    neural_net.gradient_descent(delta_error)






















def w_sum(vect, matrix):
    pass