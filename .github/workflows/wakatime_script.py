import requests

# WakaTime API URL
API_URL = 'https://wakatime.com/api/v1/users/current/summaries'

# Your WakaTime API key
API_KEY = 'waka_aa481ae6-2310-4471-9fd7-9201f6df0c64'

# Get coding activity summary for the last 7 days
response = requests.get(f'{API_URL}?api_key={API_KEY}&range=last_7_days')

# Get the URL of the coding activity graph
graph_url = response.json()['data'][0]['grand_total']['digital']['graph']

# Download the graph image
image_response = requests.get(graph_url)

# Save the graph image locally
with open('wakatime_graph.png', 'wb') as file:
    file.write(image_response.content)
