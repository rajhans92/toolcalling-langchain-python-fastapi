from langchain.tools import tool

@tool
def get_weather(city: str) -> dict:
    """
    Get current weather of a city
    """
    # call OpenWeather API here
    return {
        "temperature": 28.5,
        "description": "Clear sky",
        "humidity": 65
    }


@tool
def get_aqi(city: str) -> dict:
    """
    Get air quality index of a city
    """
    return {
        "aqi": 92,
        "level": "Moderate"
    }


@tool
def get_cost_of_living(city: str) -> dict:
    """
    Get cost of living index of a city
    """
    return {
        "rent_index": 32.5,
        "food_index": 28.1,
        "transport_index": 24.7
    }
