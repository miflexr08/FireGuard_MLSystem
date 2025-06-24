class NeuralNetwork:

    def __init__(self, input_data: [], weights: [[]]):
        assert len(input_data) == len(weights)

        self.input = input_data
        self.weights = weights
        self.current_prediction = [0, 0, 0]
        self.current_error = None

        self.ALPHA = 0.01

    def run_prediction(self):
        for i in range(self.input):

            self.current_prediction[i] = self.weight_sum(self.weights[i])

        print(f"prediction: {self.current_prediction}")

    # Each element in weights[i] corresponds to the connection strength between input neurons and the ith output neuron
    def weight_sum(self, weights, inputs=[]):
        return weights[0] * self.input[0] + weights[1] * self.input[1] + weights[2] * self.input[2]

    def calculate_error(self, real_data):
        pass

    def vect_mat_mul(self, vect, matrix):
        assert(len(vect) == len(matrix))

        for i in range(len(vect)):
            output = [0, 0, 0]
            output[i] = self.w_sum(vect, matrix[i])

        return output

    def zeros_matrix(self, size_a, size_b):
        pass

    def outer_prod(self, vec_a, vec_b):
        out = self.zeros_matrix(len(vec_a), len(vec_b))
        for i in range(len(vec_a)):
            for j in range(len(vec_b)):
                out[i][j] = vec_a[i] * vec_b[j]

        return out

    def gradient_descent(self):
        pass


# error = [0, 0, 0]
# delta = [0, 0, 0]
#
# for i in range(len(real_output)):
#     error[i] = (pred[i] - real_output[i]) ** 2
#     delta[i] = pred[i] - real_output[i]
#
# weight_deltas = outer_prod(input_data, delta)
