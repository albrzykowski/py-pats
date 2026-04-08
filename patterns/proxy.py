import time

class WeatherAPI:
    def get_temperature(self, city):
        print(f"Fetching temperature for {city} from API...")
        time.sleep(1)
        return 20

class WeatherAPIProxy:
    def __init__(self):
        self.api = WeatherAPI()
        self.cache = {}

    def get_temperature(self, city):
        if city in self.cache:
            print(f"Returning cached temperature for {city}")
            return self.cache[city]
        temp = self.api.get_temperature(city)
        self.cache[city] = temp
        return temp

proxy = WeatherAPIProxy()
print(proxy.get_temperature("London"))
print(proxy.get_temperature("London"))
print(proxy.get_temperature("Paris"))
