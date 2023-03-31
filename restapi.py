import requests

# Prompt the user to enter a positive number less than 100
while True:
    num_requests = int(input("Enter a positive number less than 100: "))
    if 0 < num_requests < 100:
        break

# Send the requested number of requests to the RandomUser API and print the names of the users
for i in range(num_requests):
    response = requests.get('https://randomuser.me/api/')
    if response.ok:
        data = response.json()['results'][0]['name']
        print(f"{i+1}. {data['title']} {data['first']} {data['last']}")
    else:
        print(f"Error: {response.status_code}")
