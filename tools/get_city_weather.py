from langchain.tools import tool


@tool
def get_city_weather(city: str) -> str:
    """
    Get traffic information for a city.

    Examples:
    - Delhi
    - Bangalore
    - Mumbai
    """

    return f"Temperature in {city} is 28 degrees"
