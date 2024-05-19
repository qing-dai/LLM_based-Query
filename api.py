import requests

# Define the URL for the API endpoint
api_url = 'https://uf9t072wj5ki2ho4.eu-west-1.aws.endpoints.huggingface.cloud/generate'

# Define the parameters
params = {
    "inputs": "Howdy!",
    "parameters": {
        "do_sample": False,
        "max_new_tokens": 40
    }
}

try:
    # Make the GET request
    response = requests.post(api_url, json=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Try to parse the JSON response
        data = response.json()
        print(data)
    else:
        # Print the status code and response text if the request failed
        print(f"Request failed with status code: {response.status_code}")
        print("Response text:", response.text)

except requests.exceptions.RequestException as e:
    # Print any request exceptions that occur
    print(f"An error occurred: {e}")
