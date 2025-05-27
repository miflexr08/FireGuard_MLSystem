# Implement weight correction for multiple weights
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
    

    def calculate_error(self):

        try:
            prediction = np.dot(self.inputs, self.weights)
            delta_error = prediction - self.fire_propagation_chance

            if delta_error < self.error_limit:
                print("Function approximated")
                print(f"Weight values: {self.weights}")

            error = (prediction - self.fire_propagation_chance) ** 2
            print(f"Quadratic medium error: {error}")
            # Explain 'Quadratic medium error' here:

        except:
            print("Invalid input information")


        



    

    


