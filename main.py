import requests
import json

# Replace with your bot's API endpoint URL
api_endpoint = "https://infoinnovator.azurewebsites.net/"

headers = {
    "Content-Type": "application/json"
}

# Example of a POST request
with open('test_convo.json', 'r') as file:
    data = json.load(file)
    response = requests.post(url=api_endpoint, data=data, headers=headers, json=file)


# Checking the response
if response.status_code == 200:
    print("Success! Response from the server:")
    print(response.text)
else:
    print(f"Failed to reach the server. Status code: {response.status_code}")
    print(response.text)

# If your API requires a POST request with data, use the following:
# response = requests.post(api_endpoint, json={"key": "value"})
# Don't forget to replace {"key": "value"} with your actual data




