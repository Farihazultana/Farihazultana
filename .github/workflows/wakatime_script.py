import requests

# WakaTime API URL
API_URL = 'https://wakatime.com/api/v1/users/current/summaries'

# Your WakaTime API key
API_KEY = 'waka_88da5b3f-1248-4f2a-9d6a-922df27eceaf'

# Get coding activity summary for the last 7 days
response = requests.get(f'{API_URL}?api_key={API_KEY}&range=last_7_days')

# Get the URL of the coding activity graph
graph_url = response.json()['data'][0]['grand_total']['digital']['graph']

# Download the graph image
image_response = requests.get(graph_url)

# Save the graph image locally
with open('wakatime_graph.png', 'wb') as file:
    file.write(image_response.content)
