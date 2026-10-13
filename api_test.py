import requests
import json

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()

    data = response.json()

    city_name = input("Enter city name: ")
    results = []
    for item in data:
        if item["address"]["city"] == city_name:
            results.append({
                "name": item["name"],
                "email": item["email"],
                "company": item["company"]["name"]
            })
    if len(results) == 0:
        print("No user found")    
    else:
        print(results)
    with open("results.json", "w") as file:
        json.dump(results, file)
    print("Git workflow practice")


except requests.exceptions.RequestException as error:
    print("Request failed", error)