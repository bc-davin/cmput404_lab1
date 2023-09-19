import requests

def main():
    url = "https://raw.githubusercontent.com/bc-davin/cmput404_lab1/main/version_check.py"

    try:
        response = requests.get(url)
        response.raise_for_status() 
        if response.status_code==200:
            source_code=response.text
            print(source_code)
        #print(f"Status Code: {response.status_code}")
        #print(f"Google Homepage Content:\n{response.text[:1000]}")  

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


