import requests
import os

# query input
query = input("Enter a search term: ")

# Pexels API
pexels_url = f"https://api.pexels.com/v1/search?query={query}&per_page=10"
pexels_headers = {"Authorization": "25TnILoz6ZxgnPUuBELrT82rWzpyVpLKAYLY6MuYvmX5lHCIh5srRWGC"}
pexels_response = requests.get(pexels_url, headers=pexels_headers).json()

# create a folder to store the images
if not os.path.exists(query):
    os.makedirs(query)

# download images from Pexels
for photo in pexels_response["photos"]:
    photo_url = photo["src"]["original"]
    photo_filename = os.path.join(query, f"{photo['id']}.jpg")
    photo_response = requests.get(photo_url)
    with open(photo_filename, "wb") as f:
        f.write(photo_response.content)
    print(f"Downloaded {photo_filename} from Pexels")


#####################################################
# Unsplash API
##################################################
unsplash_url = f"https://api.unsplash.com/search/photos?query={query}&per_page=10"
unsplash_headers = {"Authorization": "Client-ID UIgDjp2fi4yDfb0j4kIxppkYdKvAogLUZD1e3URpr_k"}
unsplash_response = requests.get(unsplash_url, headers=unsplash_headers)

# check if the API request was successful
if unsplash_response.status_code != 200:
    print(f"Error: Unsplash API returned status code {unsplash_response.status_code}")
    print(unsplash_response.json())
    exit()

# check if the response contains the expected keys
unsplash_response_json = unsplash_response.json()
if "results" not in unsplash_response_json:
    print("Error: 'results' key not found in Unsplash API response")
    print(unsplash_response_json)
    exit()

# download images from Unsplash
for photo in unsplash_response_json["results"]:
    photo_url = photo["urls"]["raw"]
    photo_filename = os.path.join(query, f"{photo['id']}.jpg")
    photo_response = requests.get(photo_url)
    with open(photo_filename, "wb") as f:
        f.write(photo_response.content)
    print(f"Downloaded {photo_filename} from Unsplash")