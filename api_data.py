# API - Application Programming Interface It's like a helper between us and a website's data.

# API Data Collection Example using PokeAPI


import requests
import pandas as pd

data_list = []

# Loop through first 10 Pokémon (We can increase the range)
for i in range(1, 11):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    data = response.json()

    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    base_experience = data["base_experience"]

    data_list.append({
        "Name": name,
        "Height": height,
        "Weight": weight,
        "Base Experience": base_experience
    })

# Convert to DataFrame
df = pd.DataFrame(data_list)

# Save to CSV file
df.to_csv("api_data.csv", index=False)
print(" Pokémon data collected and saved successfully!")
print(df.head())
