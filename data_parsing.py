import requests

api_url = "https://www.freshproduce.com/api/search/track"
params = {
    "query": "",
    "hitId": "_c61e39ee-70b3-44e9-a3bb-80be3a0882bf_en",
    "trackId": "f78nDB7yKKJsKORPETZ7jg=="
}
headers = {
    "User-Agent": "Mozilla/5.0"  # Mimic a real browser
}

response = requests.get(api_url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Print the JSON structure, so you can decide how to extract URLs
    import json
    print(json.dumps(data, indent=2))

    # If data contains URLs, say in data['results']:
    if "results" in data:
        for item in data["results"]:
            print(item.get("url"))  # Or adjust this key as needed

else:
    print("Failed to retrieve data:", response.status_code)
