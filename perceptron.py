import numpy as np

class Perceptron:

    def __init__(self, entries : list, initial_weights : list, goal : float, error_limit=0.002, alpha=0.01):
        self.inputs = np.array(entries)
        self.weights = np.array(initial_weights)
        self.fire_propagation_chance = goal
        self.error_limit = error_limit
        self.alpha = alpha

        self.error_increases = 0
        self.current_error = 0


    def make_prediction(self) -> str | None:

        assert len(self.inputs) == len(self.weights)

        prediction = np.dot(self.inputs, self.weights)
        delta_error = prediction - self.fire_propagation_chance
        self.current_error = delta_error
        print(f"delta_error: {self.current_error}")

        if abs(delta_error) <= self.error_limit:
            print("\n\n")
            print("-----------------------------")

            print(f"Right Weights: {self.weights}")
            print(f"Right prediction: {prediction}")

            print("-----------------------------")
            return "System Balanced"

        print(f"Prediction: {prediction}")
        if abs(delta_error) > self.current_error:
            if self.error_increases == 3:
                print(f"error increases: {self.error_increases}")
                return None

            self.error_increases += 1

        mean_squared_error = delta_error ** 2
        print(f"Mean squared error: {mean_squared_error}")
        # What is Mean squared error?
        """
        Mean squared error Explanation:

        """

        # A New Vector Containing Derivatives
        derivatives = np.multiply(self.inputs, delta_error)
        print(f"derivatives: {derivatives}")
        # What is a Derivative?
        """
        Derivative Explanation:

        """

        adjusted_derivatives = derivatives * self.alpha
        print(f"adjusted derivatives: {adjusted_derivatives}")
        new_weights = self.weights - adjusted_derivatives
        print(f"self.weights: {self.weights}")
        print(f"new_weights: {new_weights}")

        self.adjust_weights(new_weights)

        print("\n\n\n")

        message = self.make_prediction()

        return message


    def adjust_weights(self, new_weights):
        self.weights = new_weights
