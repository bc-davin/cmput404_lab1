import requests

def main():
    url = "https://www.google.com"

    try:
        response = requests.get(url)
        response.raise_for_status() 

        print(f"Status Code: {response.status_code}")
        print(f"Google Homepage Content:\n{response.text[:1000]}")  

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


