import requests

# Function to get weather data
def get_weather(city):
    api_key = "d56d9d2bb738ecff971816fbb579d022"  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the full API URL
    url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Send the request to the API
    response = requests.get(url)
    
    # Check if the city name is valid
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        # Extract and print weather details
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description'].capitalize()}")
    else:
        print("City not found, please check the name and try again.")

# Main function
def main():
    print("Weather Forecast Application")
    city = input("Enter city name: ")
    get_weather(city)

# Run the application
if __name__ == "__main__":
    main()
    
    input("Press Enter to exit...")

