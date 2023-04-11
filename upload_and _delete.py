import os
import base64
import json
import requests
import re
import shutil
import pywhatkit as kit
import time



import configparser

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
phone= config.get('DEFAULT', 'phone')



# Print the values
print(openai_API)
print(username)
print(pythonapp)
print(password)
print(domain_name)
print(phone)




# username = 'infoskin'
# pythonapp = 'WbMU BccK vXLk ZEys cYVX 3Knw'
# password = 'MMy@627175'
# domain_name= 'https://skinplus.pk/'


url = domain_name+'wp-json/wp/v2'
base_url = url+'/'
media_endpoint = 'media/'
tags_endpoint =  base_url+ 'tags'

print(url )
print(base_url)
print(media_endpoint)
print(tags_endpoint)



# exit()
# data_string = user + ':' + pythonapp
# token = base64.b64encode(data_string.encode())
# headers = {'Authorization': 'Basic ' + token.decode('utf8')}



# post_data ={} 
# added_media_ids=[]
# all_media_ids=[]
# topic =""
# tag_list=[]


# def get_featured_image(image_urls, pattern):
#     featured_image = None
#     remaining_images = []
# 
#     for url in image_urls:
#         if pattern in url:
#             featured_image = url
#         else:
#             remaining_images.append(url)
# 
#     if featured_image is None and len(image_urls) > 0:
#         featured_image = image_urls[0]
#         remaining_images = image_urls[1:]
# 
#     return featured_image, remaining_images






def copy_file(source_file, target_file):
    with open(source_file, "r", encoding="utf-8") as input_file:
        with open(target_file, "w", encoding="utf-8") as output_file:
            for line in input_file:
                output_file.write(line)
                
                
def convert_prices(text):
    
    converted_text=""
    # extract all dollar prices from the text using regular expression
    dollar_prices = re.findall(r"\$\d+(?:,\d+)?(?:\.\d+)?", text)
#     print(dollar_prices)
    if len(dollar_prices) == 0:
#         print("The list is empty")
        return text
    else:
#         print("The list is not empty")
        # convert dollar prices to Indian Rupee prices
        rupee_prices = []
        for price in dollar_prices:
            dollar_amount = float(price[1:].replace(",", ""))
            rupee_amount = int(dollar_amount * 55)
            rupee_price = "Rs" + str(rupee_amount)
            rupee_prices.append(rupee_price)

        # replace dollar prices with Rupee prices in the text
        for i, dollar_price in enumerate(dollar_prices):
            converted_text = text.replace(dollar_price, rupee_prices[i])
            
        return converted_text

    # write output to file in UTF-8 format
#     with open("output.txt", "w", encoding="utf-8") as f:
#         f.write(text)
#         

def add_whitespace_to_emojis(text):
    # Read input text from file
#     with open(filename, "r", encoding="utf-8") as f:
#         text = f.read()

    # Define the pattern to match emojis with optional skin tone and hair color modifiers
    pattern = r"(?<!\s)([\U0001F000-\U0001F9FF]+(?:[\u200d\uFE0F][\U0001F3FB-\U0001F3FF])*)"

    # Replace each match with a whitespace followed by the emoji
    new_text = re.sub(pattern, r" \1", text)

    # Define the pattern to match emojis without whitespace after them
    pattern = r"([\U0001F000-\U0001F9FF]+(?:[\u200d\uFE0F][\U0001F3FB-\U0001F3FF])*)(?!\s)"

    # Replace each match with the emoji followed by a whitespace
    new_text = re.sub(pattern, r"\1 ", new_text)
    
    return new_text

#     # Write output text to file
#     with open("output.txt", "w", encoding="utf-8") as f:
#         f.write(new_text)
# 
#     print("Output written to output.txt")
    
    

def move_folder(source_folder, destination_folder):
    """
    Moves all folders inside the source_folder to the destination_folder.
    """
    for subdir in os.listdir(source_folder):
        subdirectory_path = os.path.join(source_folder, subdir)
        if os.path.isdir(subdirectory_path):
            shutil.move(subdirectory_path, destination_folder)
            print("Moved folder", subdir, "to", destination_folder)
        


def markdown_image_url(url, title):
    """
    Returns a markdown-compatible image URL given a URL and a title.
    """
    # Format the URL and title strings

#     formatted_title = title.replace('"', '\\"')

    # Build the markdown image URL
    markdown_url = f"![{title}]({url})"

    return markdown_url


def add_images_to_headings(image_urls, input_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    headings = re.findall('##.*\n', content)

    for i, heading in enumerate(headings):
        if i < len(image_urls):
#             markdown_url= markdown_image_url(image_urls, image_urls)
            

            basename, extension = os.path.splitext(os.path.basename(image_urls[i]))

            basename = basename.replace('_', ' ')

            print(basename)  # prints "featured image1"
            markdown_url = f"![{basename}]({image_urls[i]})"
#             print("i ##############################################################=",i)
            content = content.replace(heading, heading + '\n' + markdown_url + '\n')
        else:
            break

    return content

        
        

def string_to_slug(text):
    # convert string to lowercase
    lower = text.lower()

    # remove non-alphanumeric characters
    alphanumeric_removed = re.sub(r'[^\w\s-]', '', lower)

    # replace spaces with hyphens
    hypen_replaced = re.sub(r'\s+', '-', alphanumeric_removed)

    return hypen_replaced


def get_media_id_info(media_ids):
    # Create an empty dictionary to store media ID and URL pairs
    media_info = {}

    # Create a list to store media URLs
    media_urls = []
    
    # Create a requests session and set authentication credentials
    session = requests.Session()
    session.auth = (username, pythonapp)

    # Loop through each media ID and retrieve its URL
    for media_id in media_ids:
        # Send a GET request to the media endpoint with the media ID
        response = session.get(base_url + media_endpoint + str(media_id))

        # Extract the URL from the response JSON
        url = response.json()['source_url']

        # Add the media ID and URL to the dictionary
        media_info[media_id] = url

        # Add the URL to the list
        media_urls.append(url)

    return media_info, media_urls


def get_media_url(media_info, media_id):
    # Retrieve the media URL from the dictionary using the media ID
    media_url = media_info.get(media_id)

    return media_url
        



# def upload_media_to_WP(image_path, title, alt_text):
#     print(image_path)
#     # Path to the image file to be uploaded
# 
# 
#     # Open the image file
#     with open(image_path, 'rb') as image_file:
#         
#         # Create a requests session and set authentication credentials
#         session = requests.Session()
#         session.auth = (username, password)
# #         base_url = 'https://skinplus.pk/wp-json/wp/v2/'
# #         media_endpoint = 'media/'
# 
# 
#         # Upload the image file using POST method
#         response = session.post(base_url + media_endpoint, files={'file': image_file})
# 
# 
#         #print(response.json())
#         # Get the image ID from the response JSON
#         image_id = response.json()['id']
#         
# 
#         # Update the image title and alt text using PUT method
#         data = {
#             'title': title,
#             'alt_text': alt_text
#         }
#         
#         
# 
#         response = session.put(base_url + media_endpoint + str(image_id), json=data)
# 
#         # Print the response status code
#         print(response.status_code)
#         
# #         exit()
#         if response.ok:
#             # Media file was created successfully, return the ID
#         
#             media_id = response.json()['id']
#             print("media id:", media_id, "created sucessfully")
#             added_media_ids.append(media_id)
#             all_media_ids.append(media_id)
#                 
#         else:
#             # Media file creation failed, return None
#             print("media id: XXXX creation failed")
#             return None


def update_githuber_md_content_filter(post_id, markdown_content):
    # Update post
#     post_id = 245985  # Replace with actual post ID
#     markdown_content = '# My updated post content in Markdown format 2''https://skinplus.pk/wp-json/

#     pythonapp = 'WbMU BccK vXLk ZEys cYVX 3Knw'
#     base_url='https://skinplus.pk/wp-json/'
    endpoint = base_url + 'myplugin/v1/update_post/' + str(post_id)


#     print(endpoint)

    response = requests.post(endpoint, auth=(username, pythonapp), data={'markdown_content': markdown_content})

    print(response.json())

def upload_media_to_WP(image_path, title, alt_text, filename, featured = False):
    # Open the image file
    with open(image_path, 'rb') as image_file:
        
        # Create a requests session and set authentication credentials
#         pythonapp = 'WbMU BccK vXLk ZEys cYVX 3Knw'
        session = requests.Session()
        session.auth = (username, pythonapp)
        print(password)
        # Upload the image file using POST method and set the filename
        response = session.post(base_url + media_endpoint, files={'file': image_file})
        print(response.text)
        
        # Get the image ID from the response JSON
        image_id = response.json()['id']

        # Update the image title and alt text using PUT method
        data = {
            'title': title,
            'alt_text': alt_text
        }
        
        response = session.put(base_url + media_endpoint + str(image_id), json=data)

        # Print the response status code
        print(response.status_code)
        
        if response.ok:
            # Media file was created successfully, return the ID
            # Get the filename from the full image path
            filename = os.path.basename(image_path)
            
            try:
                media_id = response.json()['id']
            except JSONDecodeError:
                print("Error: Response content is not a JSON string")
                image_id = None
                return None
    
    
            
            print("media id:", media_id, "created sucessfully")
            if "featured" in filename or featured== True:
                featured_image_id =  image_id
                print("featured_image_id                                   :", image_id )
                return featured_image_id
            else:
                added_media_ids.append(media_id)
                all_media_ids.append(media_id)
                
        else:
            # Media file creation failed, return None
            print("media id: XXXX creation failed")
            return None



def get_page_url(page_id):
    # Authentication credentials
#     base_url = 'https://skinplus.pk/wp-json/wp/v2/'
#     username = 'infoskin'
#     password = 'MMy@627175'
#     pythonapp = 'WbMU BccK vXLk ZEys cYVX 3Knw'
#     base_url = 'https://skinplus.pk'
#     page_id = 246101 # Replace with the ID of the page you want to retrieve

    # Create an authenticated session
    session = requests.Session()
    session.auth = (username, pythonapp)

    # Send a GET request to retrieve the page
    response = session.get(f"{base_url}pages/{page_id}")

    # Extract the URL from the response
    page_url = response.json()['link']

    print(page_url) # Print the page URL
    return page_url
    
    
def whatsapp_message(phone, message):
  
    # Replace with the number of your contact (including the country code)
    phone = "+923164760604"

    # Replace with the message you want to send
    message = page_url

    # Send the message using the WhatsApp desktop app
    kit.sendwhatmsg_instantly(phone, message, 10, tab_close=False)

def categories_from_markdown(markdown):
    categories = []

    lines = markdown.replace("**", "").strip().split('\n')
    current_category = None
    current_subcategory = None

    for line in lines:
        if line.startswith('- ') or line.startswith('-'):
            category_name = line[2:]
            current_category = {'name': category_name, 'subcategories': []}
            categories.append(current_category)
            current_subcategory = None
        elif line.startswith('    - ') or line.startswith('    -'):
            subcategory_name = line[6:]
            current_subcategory = {'name': subcategory_name, 'subsubcategories': []}
            current_category['subcategories'].append(current_subcategory)
        elif line.startswith('        - ') or line.startswith('        -') :
            subsubcategory_name = line[10:]
            current_subcategory['subsubcategories'].append({'name': subsubcategory_name})

    return categories




def read_post_data(json_path):
    # Read the post data from the JSON file
    with open(json_path, 'r') as f:
        post_data = json.load(f)
        print("post data", post_data)
        
    # Extract the values of each key in the dictionary
#     content = post_data.get('content')

    topic = post_data.get('topic')
    tags = post_data.get('tags')
    title = post_data.get('title')
    excerpt = post_data.get('excerpt')
    
    return  topic, tags, title, excerpt

articles_dir = 'markdown_Articles'
# subdir, dirnames, filenames in os.walk(articles_dir)
for subdir, dirnames, filenames in os.walk(articles_dir):
    # Initialize featured_image_id variable
    featured_image_id = None


    images_dir = 'images_all'
    File_image_Urls=[]
    media_urls =[]
    media_info = {}
    post_data ={} 
    added_media_ids=[]
    all_media_ids=[]
    topic =""
    tag_list=[]
    data_string = username + ':' + pythonapp
    token = base64.b64encode(data_string.encode())
    headers = {'Authorization': 'Basic ' + token.decode('utf8')}

    for dirname in dirnames:
        

        if dirname =='images_all':
             
        # For each subdirectory in the articles directory

            txt_path = os.path.join( subdir, 'article.txt')
           
#             print(txt_path)
            json_path = os.path.join( subdir, 'post_data.json')
            print(json_path)

            # Read the article text file
            # with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
#             with open(txt_path, 'r', errors='ignore') as f:
#                 article_text = f.read()

            # Read the article JSON file and extract the necessary data
            topic, tags, article_title, article_excerpt = read_post_data(json_path)
            
            images_dir = os.path.join(subdir, "images_all")
            
            
            
#             print("############################### PATHS #######################################")
#             print("Articles_dir              :",articles_dir)
#             print("subdir                    :",subdir)
#             print ("filenames                :", filenames)
#             print("dirnames                  :",dirnames)
#             print("dirname                  :",dirname)
#             print("images_dir                :",images_dir)
#             print("############################### PATHS END#######################################")
            
#            print(images_dir)
            # Find the URL of the image with a filename ending in '0'
            #error line
# #             #########################
# 
            featured_image_folder_path = os.path.join(images_dir, 'featured_image')
            print(featured_image_folder_path)

            for filename in os.listdir(featured_image_folder_path):
                file_path = os.path.join(featured_image_folder_path, filename)
                if os.path.isfile(file_path):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        print(f"First image file found: {file_path}")
                        featured_image_id = upload_media_to_WP(file_path, topic, topic, topic, featured = True)
                        print("image in featured image uploaded")
                        break
#             exit()
                    
#             exit()   
                    
            for f in os.listdir(images_dir):
                image_url = os.path.join(images_dir, f)
                if os.path.isfile(image_url ):
                    print(image_url)
                    print("file in image_dir           :",f)       
                    
                    File_image_Urls.append(image_url)
                
                    upload_media_to_WP(image_url, topic, topic, topic, featured = False)
            print("image urls list             :", File_image_Urls)
            print("media ids", all_media_ids )
            media_info, media_urls = get_media_id_info(all_media_ids)
    
#             media_url= get_media_url(all_media_ids)
            print(media_urls)
#     
# #             ##############################



#             media_urls = ['https://skinplus.pk/wp-content/uploads/2023/03/acid_peel_types_of_chemical_peels_4-2.png', 'https://skinplus.pk/wp-content/uploads/2023/03/chemical_peel_4-2-jpg.webp']
            



            article_text = add_images_to_headings(media_urls, txt_path)
#             print(article_text)
            # Call the function with the input filename
            t1 = add_whitespace_to_emojis(article_text)
#             print(t1)
            # call the function with input file name
            article_text= convert_prices(t1)
            print("######################################## prices changed from dollar to PKR ############################")
            print(article_text)
#             exit()

#             copy_file("output.txt", "article.txt")

            
            
            
            
#             exit()
            # get categories markdown
            category_path = os.path.join( subdir, 'categories.txt')
#             print(category_path)
            with open(category_path, 'r') as f:
                markdown = f.read()
            print("markdown :", markdown)
            categories = categories_from_markdown(markdown)
            
                        
#             continue
            
            
            # Do something with the article data:
            print("################################## topic #####################################")
            print('topic:', topic)
#             topic = topic
            
            print("################################## title #####################################")
            print('Article title:', article_title)
            
            print("################################## tags #####################################")
            print('Article tags:', tags)
            # Define the endpoint URLs

            # Define the list of tag names
#             tag_names = ['dermatologist', 'skin specialist', 'aesthetic dermatology', 'Botox', 'test tag']
            tag_names = tags

            # Initialize an empty array to store the tag IDs
            tag_ids = []

            # Loop over the tag names and create new tags or retrieve the IDs of existing tags
            for tag_name in tag_names:
                new_tag = {
                    'name': tag_name,
                    'description': tag_name,
                    'slug': tag_name.lower().replace(' ', '-')
                }
                tag_response = requests.post(tags_endpoint, headers=headers, json=new_tag)
#                 print("tag_response(before)               :",tag_response)
#                 print("tags_endpoint(before)              :",tags_endpoint)
#                 print("headers(before)                    :",headers)
#                 print("new_tag(before)                    :",new_tag)
                if tag_response.status_code == 201:
                    print(f'New tag {tag_name} added successfully!')
                    tag_list.append(tag_name)
                    tag_id = tag_response.json()['id']
                else:
                    tag_filter = {'search': tag_name}
#                     print("tags_endpoint(after)              :",tags_endpoint)
#                     print("headers(after)                      :",headers)
#                     print("tag_filter(after)                   :",tag_filter)
                    tag_response = requests.get(tags_endpoint, headers=headers, params=tag_filter)
                    tag_data = tag_response.json()
#                     print("tag_response(after)                 :",tag_response)
                    
                    
                    if tag_data:
                        tag_id = tag_data[0]['id']
                        print(f'Tag {tag_name} already exists. ID: {tag_id}')
                        tag_list.append(tag_name)
                    else:
                        print(f'Failed to add new tag {tag_name}. Error:', tag_response)
                        tag_id = None
                if tag_id:
                    tag_ids.append(tag_id)
            
#             exit()
            # Print the array of tag IDs
            print("Tag Ids: ",tag_ids)
            
            print("################################## excerpt #####################################")
            print('Article excerpt:', article_excerpt)
          

            print("################################## Categories #####################################")
            print('Categories: ',categories)
            #url = 'https://skinplus.pk/wp-json/wp/v2'
            # Initialize a dictionary to store the created category and subcategory IDs
            category_ids = {}
            # Loop through each category in the input
            for category in categories:
                # Check if the parent category already exists
                category_response = requests.get(f"{url}/categories?search={category['name']}", headers=headers)

                if category_response.ok and category_response.json():
                    # The parent category already exists
                    category_id = category_response.json()[0]['id']
                else:
                    # The parent category does not exist, so create it
                    new_category = {
                        'name': category['name'],
                        'slug': category['name'].lower().replace(' ', '-'),
                        'description': ''
                    }

                    response = requests.post(f"{url}/categories", headers=headers, json=new_category)
                    if response.ok:
                        # The category was created successfully
                        category_id = response.json()['id']
                        print(f"Created category '{category['name']}' with ID: {category_id}")
                    else:
                        print(f"Failed to create category '{category['name']}'. Error: {response.text}")
                        continue

                # Store the category ID in the dictionary
                category_ids[category['name']] = category_id

                # Loop through each subcategory in the current category
                for subcategory in category['subcategories']:
                    # Check if the subcategory already exists
                    subcategory_response = requests.get(f"{url}/categories?search={subcategory['name']}&parent={category_id}", headers=headers)

                    if subcategory_response.ok and subcategory_response.json():
                        # The subcategory already exists
                        subcategory_id = subcategory_response.json()[0]['id']
                    else:
                        # The subcategory does not exist, so create it
                        new_subcategory = {
                            'name': subcategory['name'],
                            'slug': subcategory['name'].lower().replace(' ', '-'),
                            'description': '',
                            'parent': category_id
                        }

                        response = requests.post(f"{url}/categories", headers=headers, json=new_subcategory)
                        if response.ok:
                            # The subcategory was created successfully
                            subcategory_id = response.json()['id']
                            print(f"Created subcategory '{subcategory['name']}' with ID: {subcategory_id}")
                        else:
                            print(f"Failed to create subcategory '{subcategory['name']}'. Error: {response.text}")
                            continue

                    # Store the subcategory ID in the dictionary
                    category_ids[f"{category['name']}_{subcategory['name']}"] = subcategory_id

                    # Loop through each subsubcategory in the current subcategory
                    for subsubcategory in subcategory['subsubcategories']:
                        # Check if the subsubcategory already exists
                        subsubcategory_response = requests.get(f"{url}/categories?search={subsubcategory['name']}&parent={subcategory_id}", headers=headers)

                        if subsubcategory_response.ok and subsubcategory_response.json():
                            # The subsubcategory already exists
                            subsubcategory_id = subsubcategory_response.json()[0]['id']
                        else:
                            # The subsubcategory does not exist, so create it
                            new_subsubcategory = {
                                'name': subsubcategory['name'],
                                'slug': subsubcategory['name'].lower().replace(' ', '-'),
                                'description': '',
                                'parent': subcategory_id
                            }

                            response = requests.post(f"{url}/categories", headers=headers, json=new_subsubcategory)
                            if response.ok:
                                # The subsubcategory was created successfully
                                subsubcategory_id = response.json()['id']
                                print(f"Created subsubcategory '{subsubcategory['name']}' with ID: {subsubcategory_id}")
                            else:
                                print(f"Failed to create subsubcategory '{subsubcategory['name']}'. Error: {response.text}")

#             print("category ids : ",category_ids)
            # Get all the values from the dictionary
            # Get all the values from the dictionary
            categories_id_values = list(category_ids.values())
            print("category ids: ", categories_id_values)
                        
            
            
            
            print("################################## Image URL #####################################")
#             print('Image URL:', image_url)
#             upload_media_to_WP(image_url, topic, topic,'featured',)
#             print("media ids", all_media_ids )
#             upload_images_folder_to_wp('./images_all')
            print("################################## Article #####################################")
            print('Article text:', article_text)
            # Create a Page.
            # Define the data for the new page
#             print(topic)
            slug= string_to_slug(topic)
            print(topic)
            print(article_text)
            print(article_excerpt)
            print("draft")
            print(slug)
            print(0)
#             print(all_media_ids[0])
# absInitialize featured_image_id variable

            # Check if featured_image_id is assigned
            if len(all_media_ids) > 0:
                featured_media = all_media_ids[0]
                if featured_image_id is None:
                    print("Not assigned")
                    featured_media = all_media_ids[0]
                else:
                    print("Assigned")
                    featured_media = featured_media
                # ... code that uses featured_media ...
            else:
                # handle the case where all_media_ids is empty
                print("no image in images_all foder")
           
                
            print(tag_ids)
            print(categories_id_values)
    
            # join the array elements with a comma
            Tags_string = ", ".join(tag_list)

            # print the resulting string
            print(Tags_string)
                        

            new_page = {
                "title": topic,
                "content": article_text,
                "excerpt": article_excerpt,
                "status": "publish",
                "slug": slug,
                "parent": 0,
                "featured_media": featured_image_id, # replace with the ID of the featured image
                "tags": tag_ids, # replace with the IDs of the tags to be added
                "categories": categories_id_values # replace with the IDs of the categories to be added
            #     "template": "page.php"
            }
            print("categoriesid added :", categories_id_values)
            # data = { 'title': 'Testing from Python' }
            r = requests.post( url + '/pages/', headers=headers, json=new_page )
            print("response :", r)
            data = r.json()
            page_id = str( data['id'] )
            print ('Page created. ID: ' + page_id)

            # Retrieve the Page.
            r = requests.get( url + '/pages/' + page_id, headers=headers )
            data = r.json()
            title = data['title']['rendered']
            print ('Page #' + page_id + ' retrieved. The title is: ' + title)
            
            
            update_githuber_md_content_filter(page_id, article_text)
            
           
            # 
            # # Update the Page.
            # data = { 'content': 'New content here' }
            # r = requests.post( url + '/pages/' + page_id, headers=headers, json=data )
            # data = r.json()
            # content = data['content']['rendered']
            # print 'Page #' + page_id + ' updated. Content set to: ' + content
            # 
            # # Delete the Page.
            # r = requests.delete( url + '/pages/' + page_id, headers=headers )
            # data = r.json()
            # print 'Page #' + page_id + ' moved to the Trash. (Well, it should be...)'
            # print 'The Page "status" is ' + data['status']

            
            #url = "https://skinplus.pk/wp-json/aioseo/v1/post"

            # set the post ID of the post you want to update
            # post_id = 245367
            #page id
            post_id = page_id

            # set the data to update the post SEO data
            data = {
                "id": post_id,
                "title": topic,
                "description": article_excerpt,
                "keywords": Tags_string,
                "og_title": title,
                "og_description": article_excerpt,
                "og_article_section": "Health & Wellness, Beauty & Personal Care, Med Spa, Dermatology, Plastic Surgery, Cosmetology, Esthetics",
                "og_article_tags": Tags_string,
                "twitter_title": title,
                "twitter_description": article_excerpt
            }

            # set the authentication credentials
#             username = "infoskin"
#             password = "MMy@627175"

            # set the headers
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

            # send the POST request
#            if pythonapppasword wont work
#             response = requests.post(url, auth=(username, password), headers=headers, data=json.dumps(data))
            response = requests.post(url, auth=(username, pythonapp), headers=headers, data=json.dumps(data))
            
            # get page url 
            page_url= get_page_url(post_id)
            
            with open('urls.txt', mode='a') as file:
                file.write(page_url+'\n')
            

            
          

            # print the response
            print(response.content)
            
#              file_path = os.path.join(articles_dir, "article.txt")
            # Example usage:
            
            # Define the source and destination folders
            

            
            print("dirnames:",  dirnames)
            time.sleep(10)  # Wait for 5 seconds
#             source_folder = articles_dir/
#             destination_folder = "./backups"
#             move_folder(source_folder, destination_folder)



# send the message as whatsapp
with open('urls.txt', mode='r') as file:
    file_contents = file.read()
    # Replace with the number of your contact (including the country code)
#     phone = "+923164760604"

    # Replace with the message you want to send
    message = file_contents
    print(message)

    #send whatsapp message 
    whatsapp_message(phone, file_contents)
            

