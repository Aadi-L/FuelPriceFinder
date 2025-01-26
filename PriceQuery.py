import requests

# URL to fetch the fuel price data
url = "https://storelocator.asda.com/fuel_prices_data.json"

# Fetch the data from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    
    # Extract the "stations" data
    stations = data.get("stations", [])
    
    # Loop through each station and extract details
    for station in stations:
        name = station.get("brand", "Unknown Brand")
        address = station.get("address", "Unknown Address")
        postcode = station.get("postcode", "Unknown Postcode")
        latitude = station.get("location", {}).get("latitude", "Unknown Latitude")
        longitude = station.get("location", {}).get("longitude", "Unknown Longitude")
        prices = station.get("prices", {})
        
        # Extract prices for specific fuel types
        e10_price = prices.get("E10", "Price Not Available")
        b7_price = prices.get("B7", "Price Not Available")
        
        # Print the extracted details
        print(f"Station Name: {name}")
        print(f"Address: {address}")
        print(f"Postcode: {postcode}")
        print(f"Location: Latitude {latitude}, Longitude {longitude}")
        print(f"Prices: E10 - {e10_price}, B7 - {b7_price}")
        print("-" * 40)
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")