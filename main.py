import requests

import requests

def check_github(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return True  # User exists
    elif response.status_code == 404:
        return False  # User does not exist
    else:
        raise Exception(f"Error checking user existence. Status code: {response.status_code}")

username = input("Enter the username to check: ")

# Check existence on various platforms
print("Checking existence on different platforms:")
print("GitHub:", check_github(username))
