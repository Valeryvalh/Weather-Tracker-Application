
def find_hottest_day(self):
        if not self.data:
            print("No data recorded yet.\n")
            return

        hottest_day = self.data[0]
        for data in self.data[1:]:
            if data.temperature > hottest_day.temperature:
                hottest_day = data

        print(f"the Hottest Day is:\n")
        print(f"Date: {hottest_day.date}\n")
        print(f"Temperature: {hottest_day.temperature}°C\n")
        print(f"Humidity: {hottest_day.humidity}%\n")
        print(f"Condition: {hottest_day.condition}\n")
        print('--------------------------') 