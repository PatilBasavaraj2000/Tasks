import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The application at {url} is UP.")
        else:
            print(f"The application at {url} is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"The application at {url} is DOWN. Error: {e}")

if __name__ == "__main__":
    app_url = "http://<your-application-url>"
    check_application_health(app_url)
