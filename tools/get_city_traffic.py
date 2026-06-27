from langchain.tools import tool


@tool
def get_city_traffic(city: str) -> str:
    """
    Get weather information for a city.

    Examples:
    - Delhi
    - Bangalore
    - Mumbai
    """

    return f"Traffic in {city} is Heavy"
