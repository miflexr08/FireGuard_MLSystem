class NeuralNetwork:

    def __init__(self, input_data: [], weights: [[]]):
        assert len(input_data) == len(weights)

        self.input = input_data
        self.weights = weights
        self.current_prediction = [0, 0, 0]
        self.current_error = None

        self.ALPHA = 0.01 # use it
        self.LIMIAR_ERROR = 0.002

    def run_prediction(self):
        for i in range(self.input):
            self.current_prediction[i] = self.weight_sum(self.weights[i])

    # Each element in weights[i] corresponds to the connection strength between input neurons and the ith output neuron
    def weight_sum(self, weights, inputs=[]):
        return weights[0] * self.input[0] + weights[1] * self.input[1] + weights[2] * self.input[2]

    def calculate_error(self, real_data):
        error = [0, 0, 0]
        for i in range(real_data):
            self.current_error[i] = self.current_prediction[i] - real_data[i]
            error[i] = self.current_error[i] ^ 2

        return error

    def gradient_descent(self):
        for i in range(input):
            error = self.current_error[i]
            gradients = self.input*error

            self.weights[i] - gradients

    def converged(self) -> bool:
        if (self.current_error[0] <= self.LIMIAR_ERROR and
                    self.current_error[1] <= self.LIMIAR_ERROR and
                        self.current_error[2] <= self.LIMIAR_ERROR):
            print("Neural net has converged")
            return True

        print("Not converged yet")
        return False


    # def vect_mat_mul(self, vect, matrix):
    #     assert(len(vect) == len(matrix))
    #
    #     for i in range(len(vect)):
    #         output = [0, 0, 0]
    #         output[i] = self.w_sum(vect, matrix[i])
    #
    #     return output

    #def outer_prod(self, vec_a, vec_b):
    #     out = self.zeros_matrix(len(vec_a), len(vec_b))
    #     for i in range(len(vec_a)):
    #         for j in range(len(vec_b)):
    #             out[i][j] = vec_a[i] * vec_b[j]
    #
    #     return out

    # def zeros_matrix(self, size_a, size_b):
    #     pass


# ANALYSE
# weight_deltas = outer_prod(input_data, delta)
