
# Implement weight correction for multiple weights
# Create .gitignore
# Implement alpha (observe behavior before implement it)
# Create a domain class to encapsulate the Perceptron
# Create Doc about criterias for fire propagation (more technical)
import numpy as np


class Perceptron:

    def __init__(self, entries : list, initial_weights : list, goal : float, error_limit=0.002, alpha=0.01):
        print("Initializing Perceptron ")

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

        new_weights = self.weights - derivatives
        print(f"self.weights: {self.weights}")
        print(f"new_weights: {new_weights}")

        self.adjust_weights(new_weights)

        print("\n\n\n")

        message = self.make_prediction()

        return message


    def adjust_weights(self, new_weights):
        self.weights = new_weights


named_inputs = { "temperature": 29.0, "air humidity": 0.28, "wind speed": 14.8, "slope": 0.12 }

print(f"The current temperature is {named_inputs["temperature"]}")
print(f"The current air humidity is {named_inputs["air humidity"]}")
print(f"The current wind speed is {named_inputs["wind speed"]}")
print(f"The terrain slope is {named_inputs["slope"]}")

print("\n\n\n")

inputs = []
for key, value in named_inputs.items():
    inputs.append(value)

perceptron = Perceptron(inputs, [2.0, 0.6, .45, .21], 0.21)
result = perceptron.make_prediction()

print(f"Result: {result}")



    

    


