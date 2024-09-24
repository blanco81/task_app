import requests
from app.core.config import settings

def get_weather_info(lat: float, lon: float):   
    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            country = data["sys"]["country"]
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return {
                "country": country,
                "weather": f"{weather}, {temperature}°C"
            }
        else:
            print(f"Error obteniendo el clima: {data.get('message')}")
            return {
                "country": None,
                "weather": None
            }
    except Exception as e:
        print(f"Error en get_weather_info: {e}")
        return {
            "country": None,
            "weather": None
        }
