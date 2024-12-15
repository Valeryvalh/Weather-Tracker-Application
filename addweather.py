import datetime
import json
file_name='file_save.json'
class Weather_data:
    def __init__(self, date, temperature, humidity, conditions):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
        self.conditions = conditions


    def to_json(self):
        return {
            "date": self.date,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "conditions": self.conditions
        }




class Options(Weather_data):
    def __init__(self):
        self.data = []


    def add_data(self):
        
        date = input("Enter the date of the day(yyyy-mm-dd)  \n")
        temperature = input("Enter the temperature (°C)\n ")
        humidity = input("Enter the humidity (%) \n ")
        conditions = input("Enter the conditions either it is rainy or sunny \n ")
        weatherday = Weather_data(date, temperature, humidity, conditions)
        self.data.append(weatherday)
       
        
        
       
   
    def load_data(self):
        try:
            with open("file_save.json", "r") as f:
                self.data = json.load(f)
                print(self.data)
        except FileNotFoundError:
            # File doesn't exist, data is empty
            pass
        


    def display_data(self):
        print("Current days and their weathers:  \n")
        for i in self.data:
             print(f"date: {i.date}\n", f"temperature: {i.temperature}°C\n", f"humidity: {i.humidity}%\n",f"conditions: {i.conditions}\n")
        print('--------------------------')     
        
    



    def search_by_date(self):
     date = input("Enter date to search (yyyy-mm-dd): \n")
     for date in self.data:
            if date.date == date:
                print(f"Date: {date.date}\n")
                print(f"Temperature: {date.temperature}°C\n")
                print(f"Humidity: {date.humidity}%\n")
                print(f"Condition: {date.conditions}\n")
            else:
                print("No data found for the specified date.\n")
            print('--------------------------')   
                

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


    def find_coldest_day(self):
        if not self.data:
            print("No data recorded yet.\n")
            return

        coldest_day = self.data[0]
        for data in self.data[1:]:
            if data.temperature < coldest_day.temperature:
                coldest_day = data

        print(f"the Coldest Day is:\n")
        print(f"Date: {coldest_day.date}\n")
        print(f"Temperature: {coldest_day.temperature}°C\n") 
        print(f"Humidity: {coldest_day.humidity}%\n")
        print(f"Condition: {coldest_day.condition}\n")
        print('--------------------------') 

def main():
        weather = Options()
        weather.load_data()
       
       
      
main()        