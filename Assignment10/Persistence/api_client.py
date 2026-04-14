import requests 
# !! REQUIRED !!
# pip install requests -- in CMD or powershell
# OR python -m pip install requests

class ApiClient:
    def fetch_city_data(self, city: str, latitude: float, longitude: float) -> dict:
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
            "forecast_days": 16
        }
        response = requests.get(url, params=params)
        data = response.json()
        temps = []
        for max_t, min_t in zip(
            data["daily"]["temperature_2m_max"],
            data["daily"]["temperature_2m_min"]
        ):
            temps.append(max_t)
            temps.append(min_t)
        return {
            "city": city,
            "temperatures": temps
        }