import requests

API_KEY = "39QDt7fVWUuPqLsPDAF3XkuDQEKiZkxN9z"
BASE_URL = "https://api.themoviedb.org/3/movie/top_rated"

def get_top_rated_movies(page=1):
    url = f"{BASE_URL}/movie/top_rated"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": page
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # raises error if request failed
    return response.json()

data = get_top_rated_movies()

for movie in data["results"]:
    print(f"{movie['title']} ⭐ {movie['vote_average']}")
