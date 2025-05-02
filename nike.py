import requests

api = "https://api.nike.com/search/suggestions/v1?country=IN&language=en-gb&count=8"

response = requests.get(api)

data = response.json()

item_with_details = data['searchTerms']

for i in range(len(item_with_details)):
    print(f'{i + 1}. {item_with_details[i]['displayText']}')

# list_of_items
# print(response)
# print(items_on_list)