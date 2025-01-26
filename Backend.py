from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL to fetch the fuel price data
FUEL_PRICE_URL = "https://storelocator.asda.com/fuel_prices_data.json"

@app.route('/api/fuel-prices', methods=['GET'])
def get_fuel_prices():
    try:
        # Fetch the data
        response = requests.get(FUEL_PRICE_URL)
        response.raise_for_status()
        data = response.json()

        # Extract and process the data
        stations = data.get("stations", [])
        processed_data = []
        for station in stations:
            processed_data.append({
                "name": station.get("brand", "Unknown Brand"),
                "address": station.get("address", "Unknown Address"),
                "postcode": station.get("postcode", "Unknown Postcode"),
                "latitude": station.get("location", {}).get("latitude", "Unknown Latitude"),
                "longitude": station.get("location", {}).get("longitude", "Unknown Longitude"),
                "e10_price": station.get("prices", {}).get("E10", "Price Not Available"),
                "b7_price": station.get("prices", {}).get("B7", "Price Not Available"),
            })

        return jsonify(processed_data)

    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch fuel prices", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
