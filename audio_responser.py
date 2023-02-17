import requests

# Set the URL of your Flask web application
url = "http://localhost:5000/command"

# Set the command to send
command = "What's the weather like today?"

# Send a POST request to the command endpoint with the command in the request body
response = requests.post(url, data={'command': command})

# Check if the request was successful
if response.status_code == 200:
    # Print the summarized response
    print(response.json()['response'])
else:
    # Print an error message
    print("Error: Request failed with status code", response.status_code)
