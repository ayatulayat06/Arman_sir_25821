# Looping through a Dictionary keys and values
capitals = {
    "Bangladesh": "Dhaka",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "UK": "London"
}


print("Country and Capital List:")
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")

    