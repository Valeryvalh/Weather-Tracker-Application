def search_weather_by_date(self):
        date = input("Enter date to search (dd-mm-yyyy): ")
        if date in self.weather_data:
            data = self.weather_data[date]
            print(f"Date: {date}")
            print(f"Temperature: {data['temperature']}")
            print(f"Humidity: {data['humidity']}")
            print(f"Conditions: {data['conditions']}\n")
        else:
            print("No weather data found for the given date.")
