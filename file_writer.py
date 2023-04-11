import os
import re
import shutil
from bing_image_downloader import downloader
import json
from slugify import slugify
from bs4 import BeautifulSoup
import emoji
import requests

import configparser




class FileWriter:
  

    def __init__(self, folder_path, folder_name, file_name):
        # Set the folder path, folder name, and file name as instance variables
        self.folder_path = folder_path
        self.folder_name = folder_name
        self.file_name = file_name

        # Ensure that the folder exists and get the path to the new versioned folder
        
        self.create_folder(self.folder_path)
        self.new_folder_path = self.ensure_folder_exists()

        # Define the path to the file in the new versioned folder
        self.file_path = os.path.join(self.new_folder_path, self.file_name)

        # Ensure that the file doesn't already exist
        self.ensure_file_does_not_exist()
    
    def create_folder(self, folder_path):
        """
        Creates a folder at the given folder path if it does not already exist.
        """
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder at {folder_path}")
        else:
            print(f"Folder at {folder_path} already exists")

    # Create the folder if it doesn't exist, or make a new version if it does
    def ensure_folder_exists(self):
        folder_version = 0
        folder_full_path = os.path.join(self.folder_path, self.folder_name)
        while os.path.exists(folder_full_path):
            folder_version += 1
            folder_name_with_version = f"{self.folder_name}_{folder_version}"
            folder_full_path = os.path.join(self.folder_path, folder_name_with_version)
        os.mkdir(folder_full_path)
        return folder_full_path

    # Check if the file exists, and make a new version of it if it does
    def ensure_file_does_not_exist(self):
        file_path = self.file_path
        if os.path.exists(file_path):
            file_version = 1
            while os.path.exists(file_path + "." + str(file_version)):
                file_version += 1
            new_file_path = file_path + "." + str(file_version)
            os.rename(file_path, new_file_path)

    # Define a function for writing to the file
    def write_to_file(self, text):
        # Open the file in append mode, creating a new file if it doesn't exist
        file_path = os.path.join(self.new_folder_path, "article.txt")
        with open(file_path, "a", encoding='utf-8', errors='ignore') as file:
            file.write(text + "\n")
#         with open(file_path, "a") as file:
           
#         with open(self.file_path, "a") as file:
            # Append the text to the file
#             file.write(text + "\n")

            
    def write_categories(self, text):
        # Open the file in append mode, creating a new file if it doesn't exist
        file_path = os.path.join(self.new_folder_path, "categories.txt")
        with open(file_path, "a") as file:
#         with open(self.file_path, "a") as file:
            # Append the text to the file
            file.write(text + "\n")
        
    
    



    def imagegenerator(self, keywords):
#         self.folder_path = self.file_path
#         self.folder_name = folder_name
        ##################################
          # Create a ConfigParser object
        config = configparser.ConfigParser()

        # Read the config file
        config.read('./config.ini')

        # Get the values from the config file and store them in variables
        openai_API = config.get('DEFAULT', 'openai_API')
        username = config.get('DEFAULT', 'username')
        pythonapp = config.get('DEFAULT', 'pythonapp')
        password = config.get('DEFAULT', 'password')
        domain_name = config.get('DEFAULT', 'domain_name')
        phone = config.get('DEFAULT', 'phone')
        Pexel_API = config.get('DEFAULT', 'Pexel_API')
        Unsplash_Access_Key = config.get('DEFAULT', 'Unsplash_Access_Key')
        pexel_images = config.getint('DEFAULT', 'pexel_images')
        Unsplash_images = config.getint('DEFAULT', 'Unsplash_images')

        # Print the values
        print(openai_API)
        print(username)
        print(pythonapp)
        print(password)
        print(domain_name)
        print(phone)
        print(Pexel_API)
        print(Unsplash_Access_Key)
        print(pexel_images)
        print(Unsplash_images)



        ###############################
        images_folder = os.path.join(self.new_folder_path,'images')

        images_all_folder = os.path.join(self.new_folder_path,'images_all')
        featured_image_folder = os.path.join(self.new_folder_path,'images_all','featured_image')
        keywords = keywords
        # Get the list of keywords as input
    #     keywords = ['dog', 'cat']
        
        # Create the images directory if it doesn't exist
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)

        # Create the images_all directory if it doesn't exist
        if not os.path.exists(images_all_folder):
            os.makedirs(images_all_folder)
            
                # Create the images directory if it doesn't exist
        if not os.path.exists(featured_image_folder):
            os.makedirs(featured_image_folder)

        # Iterate over keywords
        for keyword in keywords:
            PEXEL = os.path.join(self.new_folder_path,'images', keyword)
            UNSPLASH = os.path.join(self.new_folder_path,'images', keyword)
            # Download images using the keyword
#             downloader.download(keyword, limit=2, output_dir=images_folder)


            #unsplash


            #####################################################
            # Unsplash API
            ##################################################
            query = keyword
            print(Unsplash_images)
            unsplash_url = f"https://api.unsplash.com/search/photos?query={query}&per_page={Unsplash_images}"
            key= "Client-ID"+" " + Unsplash_Access_Key
            unsplash_headers = {"Authorization": key}
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
            
             # create a folder to store the images
            if not os.path.exists(UNSPLASH):
                os.makedirs(UNSPLASH)

            # download images from Unsplash
            for i, photo in enumerate(unsplash_response_json["results"]):
                photo_url = photo["urls"]["raw"]
                photo_id = photo["id"]
                filename = f"{query}.jpg"
                if os.path.isfile(os.path.join(UNSPLASH, filename)):
                    # append a number to the filename if it already exists
                    j = 1
                    while os.path.isfile(os.path.join(UNSPLASH, f"{query}_{j}.jpg")):
                        j += 1
                    filename = f"{query}_{j}.jpg"
                photo_filename = os.path.join(UNSPLASH, filename)
                photo_response = requests.get(photo_url)
                with open(photo_filename, "wb") as f:
                    f.write(photo_response.content)
                print(f"Downloaded {photo_filename} from Unsplash")








            #################################
            
            # Pexels API
            pexels_url = f"https://api.pexels.com/v1/search?query={keyword}&per_page={pexel_images}"
            pexels_headers = {"Authorization": Pexel_API}
            pexels_response = requests.get(pexels_url, headers=pexels_headers).json()

            # create a folder to store the images
            if not os.path.exists(PEXEL):
                os.makedirs(PEXEL)

            # download images from Pexels
            for i, photo in enumerate(pexels_response["photos"]):
                photo_url = photo["src"]["original"]
                photo_extension = os.path.splitext(photo_url)[1]
                photo_filename = os.path.join(PEXEL, f"{keyword}{i}{photo_extension}")
                while os.path.exists(photo_filename):
                    i += 1
                    photo_filename = os.path.join(PEXEL, f"{keyword} {i}{photo_extension}")
                photo_response = requests.get(photo_url)
                with open(photo_filename, "wb") as f:
                    f.write(photo_response.content)
                print(f"Downloaded {photo_filename} from Pexels")
                
                
            #unsplash 
            
# #             slugified_text = slugify(keyword)
#             keyword = string_to_slug(keyword)
#             # Remove emojis from input string
#             clean_text = re.sub(emoji.emoji_pattern, '', keyword)
#             
# 
#             # Print output string without emojis
#             print(clean_str)
#             get_images(clean_str, images_folder, num_images = 10)

        # Iterate over the directories in the images folder
        for directory in os.listdir(images_folder):
            # Iterate over the files in the directory
            for j, file_name in enumerate(os.listdir(os.path.join(images_folder, directory))):
                # Construct the new file name
                new_file_name = directory + '_' + str(j + 1) + '.jpg'
                # Check if the new file name already exists in the images_all directory
                if os.path.exists(os.path.join(images_all_folder, new_file_name)):
                    # If it exists, delete the existing file before copying the new file
                    os.remove(os.path.join(images_all_folder, new_file_name))
                # Copy the file to the images_all folder
               
                shutil.copy(os.path.join(images_folder, directory, file_name), os.path.join(images_all_folder, new_file_name))
                
                



                # Set the directory path
                directory_path = images_all_folder

                # Get a list of file names in the directory
                file_names = os.listdir(directory_path)

                # Loop through the file names and replace spaces with underscores
                for file_name in file_names:
                    if ' ' in file_name:
                        new_file_name = file_name.replace(' ', '_')
                        os.rename(os.path.join(directory_path, file_name), os.path.join(directory_path, new_file_name))
        # Set the paths to the folders
        IMAGES_ALL_DIR = images_all_folder
        FEATURED_IMAGE_DIR = os.path.join(IMAGES_ALL_DIR, "featured_image")
        print(FEATURED_IMAGE_DIR )

        # Get a list of all the images in the images_all folder
        images_all = os.listdir(IMAGES_ALL_DIR)
        print(images_all)

        # Remove the first image from the images_all list and get its full path
        first_image = os.path.join(IMAGES_ALL_DIR, images_all[1])
        print(images_all[0])
        print(first_image)
        #images_all.pop(0)

        # Create the featured_image folder if it doesn't exist
        if not os.path.exists(FEATURED_IMAGE_DIR):
            os.mkdir(FEATURED_IMAGE_DIR)
        print(FEATURED_IMAGE_DIR)
        # Move the first image to the featured_image folder
        print("FIRST IMAGE", first_image)
        print("FEATURED IMAGE FOLDER AND INSIDE IT IMAGE ",os.path.join(FEATURED_IMAGE_DIR, os.path.basename(first_image)))
        shutil.move(first_image, os.path.join(FEATURED_IMAGE_DIR, os.path.basename(first_image)))
     



    def on_data_received(self,data_chunks):
        # Check if all data is received
        if  'tags' in data_chunks and 'title' in data_chunks and 'excerpt' in data_chunks:
            
            # Combine the data chunks into a single dictionary
            post_data = {**data_chunks}
            
            Json_file_path = os.path.join(self.new_folder_path, 'post_data.json')
            # Save the post data to a JSON file
            with open(Json_file_path, 'w') as f:
                # Define the path to the file in the new versioned folder
                json.dump(post_data, f)
                
            print('Post data saved to file: post_data.json')





                        


def get_images(topic_slug, current_working_dir, num_images = 10):
    
    # This is the URL for the Unsplash search page
    url = "https://unsplash.com/s/photos/" + topic_slug

    # Send an HTTP request to the URL and store the response
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the images on the page using the img tag
    images = soup.find_all("img")
    images.pop(0) # This is a garbage file and we don't want it.
    series= 100
    # Iterate over the images and download each one
    for i in range(num_images):
        image = images[i]
        
        # Get the image URL and download it
        image_url = image["src"]
        response = requests.get(image_url)
        
        # Save the image to disk
        # The image file name is the last part of the image URL
        # For example, the image file name for https://example.com/images/image.jpg is image.jpg
        # We use the split() method to get the last part of the URL
        # and the replace() method to remove the query string from the file name
        # 

        file_name = topic_slug + str(i+series) + ".jpg"
        file_path = os.path.join(current_working_dir + '/images', file_name)
        with open(file_path, "wb") as f:
            f.write(response.content)
            print("Downloaded", file_name)
        
    return images


def string_to_slug(text):
    # convert string to lowercase
    lower = text.lower()

    # remove non-alphanumeric characters
    alphanumeric_removed = re.sub(r'[^\w\s-]', '', lower)

    # replace spaces with hyphens
    hypen_replaced = re.sub(r'\s+', '-', alphanumeric_removed)

    return hypen_replaced