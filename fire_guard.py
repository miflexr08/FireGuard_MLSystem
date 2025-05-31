from perceptron import Perceptron
from severity import Severity

# Heritage from a Generic Class (specialized classes for different purposes)
class FireGuardMLSystem:

    def __init__(self):

        # named_inputs = {"temperature": 29.0, "air humidity": 0.28, "wind speed": 14.8, "slope": 0.12}
        self._temperature = 29.0
        self._air_humidity = 0.28
        self._wind_speed = 14.8
        self._slope = 0.12

        self.perceptron = Perceptron([self._temperature, self._air_humidity, self._wind_speed, self._slope],
                                     [2.0, 0.6, .45, .21], 0.21)

        print(f""""
            - Temperature: {self._temperature}\n
            - Air humidity: {self._air_humidity}\n
            - Wind speed: {self._wind_speed}\n
            - Terrain slope: {self._slope}\n\n\n
        """)

    def classify_fire_severity(self) -> Severity:
        severity = self.perceptron.make_prediction()
        print(f"severity: {severity}")
        return Severity.CRITICAL