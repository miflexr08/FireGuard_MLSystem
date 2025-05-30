# Implement weight correction for multiple weights
# Create .gitignore
# Implement alpha (observe behavior before implement it)
# Create a domain class to encapsulate the Perceptron
# Create Doc about criterias for fire propagation (more technical)

import numpy as np

named_inputs = { "temperature": 29.0, "air humidity": 0.28, "wind speed": 14.8, "slope": 0.12 }

print(f"The current temperature is {named_inputs["temperature"]}")
print(f"The current air humidity is {named_inputs["air humidity"]}")
print(f"The current wind speed is {named_inputs["wind speed"]}")
print(f"The terrain slope is {named_inputs["slope"]}")

fire_propagation_chance = 0.21 # that's the goal


class Perceptron():

    def __super__(self, inputs, initial_weights, goal):
        print("Initializing Perceptron ")

        self.inputs = np.array(inputs)
        self.weights = np.array(initial_weights)
        self.fire_propagation_chance = goal 
        self.error_limit = 0.02 # What is a good error limit?
        self.alpha = 0.01

        self.current_error = 0
        self.error_increases = 0
    

    def make_prediction(self):

        try:
            prediction = np.dot(self.inputs, self.weights)
            delta_error = prediction - self.fire_propagation_chance

            if delta_error <= self.error_limit:
                return 1

            if abs(delta_error) > self.current_error:
                if (self.error_increases + 1) == 3:
                    print(f"error increases: {self.error_increases}")
                    raise Exception("Error is growing...")
                
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

            self.weights = new_weights
            self.make_prediction()

        except e:
            print(f"Error: {e}")
            return 0


# How To Generate the Weights
perceptron = Perceptron(named_inputs.values(), list(), fire_propagation_chance)
result = perceptron.make_prediction()


    

    


