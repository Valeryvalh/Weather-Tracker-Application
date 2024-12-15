
# Step 1: Define a list to store weather data
weather_data = []

# Step 2: Display menu options in a loop
while True:
    # Display menu options
    print("\nWeather Tracker Menu:")
    print("1. Add Weather Data")
    print("2. View Weather History")
    print("3. Search Weather by Date")
    print("4. Find Hottest Day")
    print("5. Find Coldest Day")
    print("6. Export Data")
    print("7. Exit")

    # Get user choice
    choice = input("Choose an option (1-7): ")

    # Step 3: Option to add weather data
    if choice == "1":
        # Input weather details
        date = input("Enter the date (YYYY-MM-DD): ")
        temp = float(input("Enter the temperature (°C): "))
        humidity = float(input("Enter the humidity (%): "))
        conditions = input("Enter the weather conditions (e.g., sunny, rainy): ")

        # Save the data as a dictionary
        weather_data.append({
            "date": date,
            "temperature": temp,
            "humidity": humidity,
            "conditions": conditions
        })
        print("Weather data added successfully!")

    # Step 4: View all recorded weather history
    elif choice == "2":
        print("\nWeather History:")
        if not weather_data:
            print("No data available.")
        else:
            for entry in weather_data:
                print(f"Date: {entry['date']}, Temperature: {entry['temperature']}°C, Humidity: {entry['humidity']}%, Conditions: {entry['conditions']}")

    # Step 5: Search weather data by date
    elif choice == "3":
        search_date = input("Enter the date to search (YYYY-MM-DD): ")
        found = False
        for entry in weather_data:
            if entry["date"] == search_date:
                print(f"Date: {entry['date']}, Temperature: {entry['temperature']}°C, Humidity: {entry['humidity']}%, Conditions: {entry['conditions']}")
                found = True
                break
        if not found:
            print("No data found for that date.")

    # Step 6: Find the hottest day
    elif choice == "4":
        if not weather_data:
            print("No data available.")
        else:
            hottest_day = max(weather_data, key=lambda x: x["temperature"])
            print(f"The hottest day is {hottest_day['date']} with {hottest_day['temperature']}°C.")

    # Step 7: Find the coldest day
    elif choice == "5":
        if not weather_data:
            print("No data available.")
        else:
            coldest_day = min(weather_data, key=lambda x: x["temperature"])
            print(f"The coldest day is {coldest_day['date']} with {coldest_day['temperature']}°C.")

    # Step 8: Export data to a file
    elif choice == "6":
        file_name = "save.txt"
        with open(file_name, "r+") as file:
            for entry in weather_data:
                file.write(f"Date: {entry['date']}, Temperature: {entry['temperature']}°C, Humidity: {entry['humidity']}%, Conditions: {entry['conditions']}\n")
        print(f"Data successfully exported to {file_name}.")

    # Step 9: Exit the program
    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break

    # Step 10: Handle invalid input
    else:
        print("Invalid option. Please choose a number between 1 and 7.")