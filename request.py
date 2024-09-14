import requests

# URL of the JavaScript file you want to download
url = 'https://web.facebook.com/?_rdc=1&_rdr'

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a local file in write-binary mode and write the content
    with open('downloaded_file.js', 'wb') as file:
        file.write(response.content)
    print('JavaScript file downloaded and saved as downloaded_file.js')
else:
    print(f'Failed to retrieve the file. Status code: {response.status_code}')
