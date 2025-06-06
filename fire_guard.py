from perceptron import Perceptron
from severity import Severity

# Heritage from a Generic Class (specialized classes for different purposes)
class FireGuardMLSystem:

    def __init__(self):

        # named_inputs = {"temperature": 29.0, "air humidity": 0.28, "wind speed": 14.8, "slope": 0.12}
        self._temperature = 29.0 # celsius
        self._air_humidity = 0.28 # percentual
        self._wind_speed = 14.8 # m/s
        self._slope = 0.12 # percentual, angle
        self._mitigation_score = 0.5

        self.perceptron = Perceptron(
        [self._temperature, self._air_humidity, self._wind_speed, self._slope, self._mitigation_score],
        [2.0, -0.6, .45, .21, -0.2], 0.21, 0.02, 0.001)

        print(f""""
            - Temperature: {self._temperature}\n
            - Air humidity: {self._air_humidity}\n
            - Wind speed: {self._wind_speed}\n
            - Terrain slope: {self._slope}\n\
            - Mitigation Score: {self._mitigation_score}\n\n
        """)

    def classify_fire_severity(self) -> Severity:
        prediction_info = self.perceptron.make_prediction()
        if prediction_info is None:
            print("System is divergent")

        print("\n\n")
        print("-----------------------------")

        print(f"Right Weights: {prediction_info[1]}")
        print(f"Right prediction: {prediction_info[0]}")

        print("-----------------------------")

        return self.get_severity(prediction_info[0])

    def get_severity(self, prediction) -> Severity:
        if prediction >= 0.75:
            return Severity.Critical
        elif prediction >= 0.5:
            return Severity.Attention
        elif prediction >= 0.25:
            return Severity.Ok
        else:
            return Severity.Normal


# Test One
# self.perceptron = Perceptron([self._temperature, self._air_humidity, self._wind_speed, self._slope],
#                                     [2.0, 0.6, .45, .21], 0.21, 0.02, 0.001)
# Right Weights: [ 0.23129666  0.58292286 -0.4526486   0.20268123]
# Right prediction: 0.19594414957875095

# Test Two
# self.perceptron = Perceptron([self._temperature, self._air_humidity, self._wind_speed, self._slope],
#                                     [2.0, -0.6, .45, .21], 0.21, 0.02, 0.001)
# Right Weights: [ 0.24048996 -0.61698837 -0.44795685  0.20271927]
# Right prediction: 0.19601720855079427

# Test Three (changing weights completely to watch the system balanced itself in a different way
# using different updated weights)
# self.perceptron = Perceptron([self._temperature, self._air_humidity, self._wind_speed, self._slope],
#                                     [6.0, -0.21, 1.45, .001], 0.21, 0.02, 0.001)
# Right Weights: [ 0.66059887 -0.26155284 -1.27493575 -0.02109407]
# Right prediction: 0.21255215006792083

# Test Four (adding mitigation_score)
# self.perceptron = Perceptron(
#        [self._temperature, self._air_humidity, self._wind_speed, self._slope, self._mitigation_score],
#        [2.0, -0.6, .45, .21, -0.2], 0.21, 0.02, 0.001)
# Right Weights: [ 0.24363547 -0.616958   -0.44635155  0.20273228 -0.23028215]
# Right prediction: 0.19586409966576085