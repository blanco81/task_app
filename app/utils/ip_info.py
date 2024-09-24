import requests

def get_ip_info(ip: str):   
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        return latitude, longitude
    except Exception as e:
        print(f"Error obteniendo información de IP: {e}")
        return None, None

