from pydantic import BaseModel


class WeatherInfo(BaseModel):
    temperature: float
    description: str
    humidity: int

class AQIInfo(BaseModel):
    aqi: int
    level: str

class CostOfLiving(BaseModel):
    rent_index: float
    food_index: float
    transport_index: float

class CityInfoResponse(BaseModel):
    city: str
    weather: WeatherInfo
    aqi: AQIInfo
    cost_of_living: CostOfLiving
