class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(self, observer):
        pass
    def removeObserver(self, observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers(self):
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("\nCurrent conditions:", self.temperature,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)

# Implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay(Observer):
    """
    The StatisticsDisplay class keeps track of the min/average/max measurements and displays them.
    """
    def __init__(self, weatherData):
        self.current = {
            "Temperature": { "Min": 0.0, "Max": 0.0, "Mean": 0.0, "Sum": 0.0 },
            "Humidity": { "Min": 0.0, "Max": 0.0, "Mean": 0.0, "Sum": 0.0},
            "Pressure": { "Min": 0.0, "Max": 0.0, "Mean": 0.0, "Sum": 0.0 },
        }

        self.categories = ["Temperature", "Humidity", "Pressure"]
        self.stats = ["Min", "Max", "Mean"]
        self.logCount = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        newValues = [temperature, humidity, pressure]

        self.logCount += 1 # update total count of log entries

        # For each category, update running total, min, max, and mean
        for i, category in enumerate(self.categories):
            self.addSum(category, newValues[i])
            self.current[category]["Min"] = self.getMin(category, newValues[i])
            self.current[category]["Max"] = self.getMax(category, newValues[i])
            self.current[category]["Mean"] = self.getMean(category)

        self.display()

    def getMin(self, category, newValue):
        currentValue = self.current[category]["Min"]
        if self.logCount == 1:
            currentValue = newValue
        return min(currentValue, newValue)

    def getMax(self, category, newValue):
        currentValue = self.current[category]["Max"]
        return max(currentValue, newValue)

    def getMean(self, category):
        total = self.current[category]["Sum"]
        return total / self.logCount

    def addSum(self, category, newValue):
        self.current[category]["Sum"] += newValue

    def display(self):
        print("Running Statistics:", end="")
        for key, val in self.current.items():
            print(f"\n  {key}: ", end="")
            for each in val:
                if each != "Sum":
                    print(f"{each}: {val[each]} ", end="")


class ForecastDisplay(Observer):
    """
    The ForecastDisplay class shows the weather forcast based on the current
    temperature, humidity and pressure.

    Uses the following formulas:
    forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
    forecast_hum = humidity - 0.9 * humidity
    forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
    """
    def __init__(self, weather_data):
        self.forecast_temp = 0
        self.forecast_hum = 0
        self.forecast_pressure = 0

        self.weather_data = weather_data # save the ref in an attribute.
        weather_data.registerObserver(self) # register the observer
                                           # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_hum = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print("\nForecast conditions:", self.forecast_temp,
              "F degrees and", self.forecast_hum,"[%] humidity",
              "and pressure", self.forecast_pressure)

class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        stats_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.removeObserver(stats_display)
        weather_data.removeObserver(forecast_display)

        weather_data.setMeasurements(120, 100,1000)



if __name__ == "__main__":
    w = WeatherStation()
    w.main()
    # Running returns this:
    # Current conditions: 80 F degrees and 65 [%] humidity and pressure 30.4
    # Current conditions: 82 F degrees and 70 [%] humidity and pressure 29.2
    # Current conditions: 78 F degrees and 90 [%] humidity and pressure 29.2
