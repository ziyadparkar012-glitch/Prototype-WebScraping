import requests


BASE_URL = "https://propertyapi.co/api/v1"


def get_property_data(address: str, api_key: str):
    url = f"{BASE_URL}/parcels/search-by-address"

    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
    }

    params = {
        "address": address
    }

    response = requests.get(url, headers=headers, params=params, timeout=30)
    data = response.json()

    if response.status_code != 200 or data.get("status") != "ok":
        raise Exception(f"API error: {data}")

    return data.get("data")