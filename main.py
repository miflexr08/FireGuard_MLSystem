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

    def __super__(inputs, initial_weights, goal):
        print("Initializing Perceptron ")

        self.inputs = np.array(inputs)
        self.weights = np.array(initial_weights)
        self.fire_propagation_chance = goal 
        self.error_limit = 0.02 # What is a good error limit?
        self.alpha = 0.01

        self.current_error = 0
        self.bigger_error_times = 0
    

    def make_prediction(self):

        try:
            prediction = np.dot(self.inputs, self.weights)
            delta_error = prediction - self.fire_propagation_chance

            if delta_error <= self.error_limit:
                return 1

            delta_error = prediction - self.fire_propagation_chance
            if delta_error > self.current_error:
                self.bigger_error_times += 1
                if self.bigger_error_times == 3:
                    raise Exception("Error is growing...")

            mean_squared_error = delta_error ** 2
            
            print(f"Mean squared error: {mean_squared_error}")
            # What is Mean squared error?
            """
            Mean squared error Explanation:
            
            """

            # A new vector with the derivatives 
            derivatives = np.multiply(self.inputs, delta_error)

            print(f"derivatives: {derivatives}")

            new_weights = self.weights - derivatives

            print(f"new_weights: {new_weights}")

            self.weights = new_weights

            self.make_prediction()

        except e:
            print(f"Error: {e}")


        



    

    


