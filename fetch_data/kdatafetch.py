import requests
import time

def fetch_data():
    """Fetch data from the specified URL."""
    # url = "http://data-server:9092/data"  # Use host.docker.internal to access the host machine
    url = "http://host.docker.internal:9092/data"

    try:
        
        while True:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()  # Parse JSON response
            print("Fetched Data:", data)
            time.sleep(10)
        # return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    fetch_data()
