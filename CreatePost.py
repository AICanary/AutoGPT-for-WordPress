import openai
from file_writer import FileWriter
from bing_image_scraper import imagegenerator
import json
import os
import re
import markdown
import configparser

from chatGPT_debugger.chatGPT_debugger import debug



import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('./config.ini')

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
Catagories = config.get('DEFAULT', 'Catagories')


# Print the values
print(openai_API)
print(username)
print(pythonapp)
print(password)
print(domain_name)




# import shutil
data_chunks = {}
@debug
class PostGenerator:
    def __init__(self,topic):
        self.Full_Article= ""
#         self.TOPIC = topic
        TOPIC = topic
        # Set up a dictionary to store the data
        
        openai.api_key = openai_API
        print("your api key is                 ",openai.api_key)
#         TOPIC="HIFU hairfall treatment in Lahore"


        SECTIONS_COUNT=20
        PARAGRAPHS_PER_SECTION=1
        FAQ =10
        
        
        
        
        LANGUAGE="english"
        # creative
        WRITING_STYLE="clear, informative, and professional, with accessible language and a compassionate approach"
        WRITING_TONE=" evidence-based information and recommendations,  be structured in a logical and easy-to-follow manner"
        # Define the folder path, folder name, and file name
        
        
        # Define the folder name
        folder_name = "markdown_Articles"

        # Get the current directory
        current_dir = os.getcwd()

        # Create the folder path
        FOLDER_PATH = os.path.join(current_dir, folder_name)
        
        # Check if the folder exists
        if not os.path.exists(FOLDER_PATH):
            # Create the folder if it does not exist
            os.mkdir(FOLDER_PATH)
            
        # Print the folder path
        print("Folder path:", FOLDER_PATH)


#         FOLDER_PATH = r"D:\code\Python\markdown_Articles_Generator\markdown_Articles"
        FOLDER_NAME = TOPIC
        FILE_NAME = TOPIC + ".txt"
        folder_path_to_remove = os.path.join(FOLDER_PATH, FOLDER_NAME)

        # Create an instance of the FileWriter class with the folder path, folder name, and file name
        
        self.file_writer = FileWriter(FOLDER_PATH, FOLDER_NAME, FILE_NAME)
        print(self.file_writer)
#         exit()
        TITLE=""
        SECTIONS=[]
#         LANGUAGE="english"
#         # creative
#         WRITING_STYLE="informative"
#         WRITING_TONE="trustful"
        #############

#         print("#####################   HEADINGS 2 ###############################")
#         Full_Article= ""
#         SECTIONS_PROMPT=f"Act as a dermatologist; write consective headings and subheadings to break down the information on the topic of 'botox training in lahore' ; that has  to be clear, informative, and professional, with accessible language and a compassionate approach. with evidence-based information and recommendations,  be structured in a logical and easy-to-follow manner."
#         SECTIONS=self.result(SECTIONS_PROMPT)
#         MORE_SECTIONS = "\n"
# #         SECTIONS = "## Introduction" + SECTIONS + MORE_SECTIONS + "## Conclusion"
#         print(SECTIONS)
#         exit()
        
        

        print("###################### Topic #########################")
        receive_data_chunk({'topic': TOPIC})
        print("topic : ",TOPIC)
        
#         ###########################################
        print("###################### category- single level ##################################")
        single_level_category_prompt= f"for the Topic {TOPIC}. for wordpress website; choose most relevants from following catagories: {Catagories}.  give only the answer in a single-level markdown unordered list format(- ). don't use any brackets."
        print("category prompt                   :", single_level_category_prompt)
        category_CSV_list= categories_result=self.result(single_level_category_prompt)
#         singlelevel_category_list= self.clean_string(category_CSV_list)
        self.file_writer.write_categories(category_CSV_list)
        print(category_CSV_list)
#         exit()
#         ###########################################
        



# for multilevel- categories 
#         print("###################### Categories - multiple levels #########################")
# #         TOPIC = "hydrafacial lahore"
#         category_prompt= f"given the title: {TOPIC}."
#         category_prompt_example = '''
#         [For location based directory service.  make categories and sub-categories and sub-sub-categories in following markdown format: for example for "Best Acne Treatment in Allama Iqbal Town Lahore"
# 
#         - Lahore
#           - Subcategories:
#             - Treatments
#               - Sub-subcategories:
#                 - Chemical Peels
#                 - Microdermabrasion
#             - Dermatologists
#               - Sub-subcategories:
#                 - Acne Specialists
#                 - General Dermatologists
#         - Allama Iqbal Town
#           - Subcategories:
#             - Dermatologists
#               - Sub-subcategories:
#                 - Acne Specialists
#                 - General Dermatologists
#             - Skincare Products
#               - Sub-subcategories:
#                 - Cleansers
#                 - Toners
#             - Acne Treatment
#               - Sub-subcategories:
#                 - Topical Treatments
#                 - Oral Medications
#               ]
#         '''
#         category_complete_prompt = category_prompt_example + category_prompt
# #         print("category_complete_prompt  :  ", category_complete_prompt)
#         categories_result=self.result(category_complete_prompt)
#         self.file_writer.write_categories(categories_result)
#         print(categories_result)
#         exit()

      
      
#       
#         ###############################################
#         
        print("###################### Image Description #########################")
        IMAGE_DESCRIPTION_PROMPT= f"For the {TOPIC}, give 2 generic comma seperated key-phrase to search for images on internet."
        IMAGE_DESCRIPTION=self.result(IMAGE_DESCRIPTION_PROMPT)
        print(IMAGE_DESCRIPTION)
        string_list = self.clean_string(IMAGE_DESCRIPTION)
        
#         string_list.append(TOPIC)
        print(string_list)
#         self.file_writer.write_to_file(string_list)
        self.file_writer.imagegenerator (string_list)
        
#         imagegenerator(string_list)
#         exit()

        
        
        ################################################
        print("#####################   STORY  ###############################")
        STORY_PROMPT=f"write an interesting story on the topic of {TOPIC}. use character names from Pakistan. Bold \"important keywords and phrases\" with markdown emphasis style ( ** ** )"
        STORY=self.result(STORY_PROMPT)
        
        STORY = STORY.lstrip()
        input_string = STORY

        # Split the input string into paragraphs
        paragraphs = input_string.split('\n\n')

        # Add the '>' character to the start of every paragraph
        formatted_paragraphs = [f">{paragraph}" for paragraph in paragraphs]

        # Join the paragraphs back into a single string
        output_string = '\n\n'.join(formatted_paragraphs)
        
        # Print the formatted string
#         print(output_string)
#         self.file_writer.write_to_file (f"### Story about {TOPIC}")
        self.file_writer.write_to_file ("\n")
        self.file_writer.write_to_file (output_string)
        print(output_string)
        self.file_writer.write_to_file ("\n")
        self.file_writer.write_to_file ("------------")
        self.file_writer.write_to_file ("\n")

        ##################################################
        print("#####################   HEADINGS  ###############################")
        
        SECTIONS_PROMPT=f"Write {SECTIONS_COUNT} consecutive headings for an article about {TOPIC}. stylize headings with (## ). Headings should be clear, informative, and professional, with accessible language and a compassionate approach"
        SECTIONS=self.result(SECTIONS_PROMPT)
        MORE_SECTIONS = "\n"
        SECTIONS = "## Introduction" + SECTIONS + MORE_SECTIONS + "## Conclusion"
        print(SECTIONS)
#         exit()
        
        






#         self.file_writer.write_to_file(SECTIONS)
        
        
        
#         exit()
#         self.file_writer.write_to_file ("\n")
#         self.file_writer.write_to_file ("------------")
#         self.file_writer.write_to_file ("\n")
        
       
#         exit()
        # Split the string into an array based on the newline character
        SECTIONS_array = SECTIONS.split('\n')

        # Remove any empty elements from the array
        SECTIONS_array = list(filter(None, SECTIONS_array))

        print("#####################   SECTIONS  ###############################")
        # Iterate over each element in the array and print it out
        for SECTION in SECTIONS_array:
            print(SECTION)
            self.write_headings(SECTION)
            

            

            #ARTICLE_PROMPT=f"Bold important keyword  using markdown emphasis (**  **). Write an article about \"{TITLE}\" in {LANGUAGE}. The article is organized by the bullet points and following headings: {SECTIONS} Write {PARAGRAPHS_PER_SECTION} paragraphs per heading. Style: {WRITING_STYLE}. Tone: {WRITING_TONE}."
            ARTICLE_PROMPT=f"[Write in simple words in context of {TOPIC}.  write {PARAGRAPHS_PER_SECTION} paragraphs. style the text as: 1.  Bold \"important and difficult words and phrases\" with markdown emphasis style ( ** ** )  2.  use un-ordered list ] {SECTION}. Style: {WRITING_STYLE}. Tone: {WRITING_TONE}."
            ARTICLE=self.result(ARTICLE_PROMPT)
            if SECTION != '## Introduction' or SECTION != "## Conclusion":
                new_paragraph = self.remove_first_sentence(ARTICLE)
            print(new_paragraph)
            self.add_section_to_Article(new_paragraph)

###########################


#             self.file_writer.write_to_file(new_paragraph)
#             self.file_writer.write_to_file ("\n")
#             self.file_writer.write_to_file ("------------")
#             self.file_writer.write_to_file ("\n")
#             print("\n")
#             print("------------")
#             print("\n")
#             
#             Full_Article= Full_Article +new_paragraph
#             Full_Article= self.text_to_markdown(Full_Article)



#######################
            
        # Convert Markdown to HTML
#         html = markdown.markdown(Full_Article)
#         print(html)
#         receive_data_chunk({'content': html})
            
            
#         on_data_received()
        
        print("#####################   FAQ  ###############################")
        FAQ_PROMPT=f"Write {FAQ} FAQ on Topic {TOPIC}. Higlight the questions with (** **). also number the questions."
        FAQ_Response=self.result(FAQ_PROMPT)
        self.write_headings("## FAQ")
        self.file_writer.write_to_file ("\n")
        self.add_section_to_Article(FAQ_Response)
        
            

        print("###################### TITLE #########################")
        SHORT_TITLE_PROMPT= f"For the {TOPIC}, write a SEO-friendly short title. Don't add qoutation marks."
        SHORT_TITLE=self.result(SHORT_TITLE_PROMPT)
        
        title= self.clean_text(SHORT_TITLE)
#         self.file_writer.write_to_file(title)
        receive_data_chunk({'title': title})
        print(title)
#         self.file_writer.write_to_file ("------------")
        
        print("###################### Keywords #########################")
        KEYWORDS_PROMPT= f"For the {TOPIC}, write a SEO-friendly keywords in comma seperate string."
        KEYWORDS=self.result(KEYWORDS_PROMPT)
        keywords = self.clean_string(KEYWORDS)
#         self.file_writer.write_to_file(KEYWORDS)
        receive_data_chunk({'tags': keywords})
#         text = KEYWORDS.replace(".", "")
        print(keywords)
        
#         exit()
##############

################

        print("###################### Excerpt #########################")
        META_DESCRIPTION_PROMPT= f"For the {TOPIC}, write a SEO-friendly meta-description.Don't add qoutation marks."
        META_DESCRIPTION=self.result(META_DESCRIPTION_PROMPT)
#         print(META_DESCRIPTION)
        excerpt= self.clean_text(META_DESCRIPTION)
#         self.file_writer.write_to_file(excerpt)
        receive_data_chunk({'excerpt': excerpt})
        print(excerpt)
        
#         
#         file_path = "path/to/my/markdown/file.md"
#         image_list = ["https://example.com/image1.jpg", "https://example.com/image2.jpg", "https://example.com/image3.jpg"]
# 
#         insert_images_in_file(file_path, image_list)

##################################

#         on_data_received()
        self.file_writer.on_data_received(data_chunks)
#         tags, title, excerpt = read_post_data()
# #         print(content)
#         print(tags)
#         print(title)
#         print(excerpt)


###################

    def write_headings(self,SECTION):
        if SECTION != '## introduction':
            self.file_writer.write_to_file(SECTION)
        self.Full_Article= self.Full_Article + SECTION
        print("\n")
        self.file_writer.write_to_file ("\n")
        self.text_to_markdown(self.Full_Article)
        
        


    def add_section_to_Article(self, new_paragraph):
        self.file_writer.write_to_file(new_paragraph)
        self.file_writer.write_to_file ("\n")
        self.file_writer.write_to_file ("------------")
        self.file_writer.write_to_file ("\n")
        print("\n")
        print("------------")
        print("\n")
        
        self.Full_Article= self.Full_Article +new_paragraph
        self.Full_Article= self.text_to_markdown(self.Full_Article)

    def remove_first_sentence(self, paragraph):
        # Split the paragraph into sentences using period as the delimiter
        sentences = paragraph.split(".")
        
        # If the first sentence is not the last sentence in the paragraph, remove it
        if len(sentences) > 1:
            first_sentence = sentences[0].strip()
            remaining_text = ".".join(sentences[1:]).strip()
            return remaining_text
        else:
            return ""
    ###########################
    def result(self, string):
        try:
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=string,
                max_tokens=3500,
                n=1,
                stop=None,
                #temperature=0.8,
                temperature=0.5,
                # top_p=0.3,
                # stream=True
            )
            message = completions.choices[0].text
            # print(message)
            return message
        except openai.Error as e:
            # handle the error here
            print("An error occurred:", e)
            print("deleting the folder")
            remove_folder()
            
            exit()
        ####################
    
    def clean_string(self, text):
        string = text
        string = string.replace(".", "").replace("\n", "").replace('"', '').replace("'", '')  # remove full stops
        string = string.strip()  # remove extra white space

        string_list = string.split(", ")  # split by commas and create a list
        lowercase_list = [s.lower() for s in string_list]
        return lowercase_list
    
    def clean_text(self, text):

        text = text.replace("\n", "").replace('"', '').replace("'", '')  # remove full stops
        text = text.strip()  # remove extra white space
        return text
    
    
    def text_to_markdown(self, text):
        markdown_text = text.replace("\n", "  \n")
        return markdown_text
                    
                    
                    

    


   # Receive data in parts using a dictionary
def receive_data_chunk(data_chunk):
  # Add the data chunk to the dictionary
  data_chunks.update(data_chunk)




# Once all data is received
def on_data_received():
    # Check if all data is received
    if  'tags' in data_chunks and 'title' in data_chunks and 'excerpt' in data_chunks and 'topic' in data_chunks :
        
        # Combine the data chunks into a single dictionary
        post_data = {**data_chunks}
        
        # Save the post data to a JSON file
        with open('post_data.json', 'w') as f:
            json.dump(post_data, f)
            
        print('Post data saved to file: post_data.json')
        
    

def read_post_data():
    # Read the post data from the JSON file
    with open('post_data.json', 'r') as f:
        post_data = json.load(f)
        
    # Extract the values of each key in the dictionary
#     content = post_data.get('content')
    topic = post_data.get('topic')
    tags = post_data.get('tags')
    title = post_data.get('title')
    excerpt = post_data.get('excerpt')
    
    return  topic, tags, title, excerpt

def remove_folder():
    """
    Remove a folder and its contents to the recycle bin
    """
    
    print("folder to remove", folder_path_to_remove)
    if os.path.exists(folder_path_to_remove):
        send2trash.send2trash(folder_path_to_remove)
        print(f"{folder_path} removed to recycle bin.")
    else:
        print(f"{folder_path} does not exist.")
        

def sections_to_json():

    text = """I. Introduction
    - Definition of Botox
    - Importance of proper training for administering Botox
    - Overview of the botox training landscape in Lahore

    II. The Benefits of Botox Training
    - Improved Patient Care
    - Increased Demand for Botox
    - Professional Advancement

    III. Conclusion
    - Summary of Key Points
    - Recommendations for Next Steps
    - Overview of the botox training landscape in Lahore
    - Recommendations for Next Steps
    - Overview of the botox training landscape in Lahore"""

    section_pattern = re.compile(r'^([IVXivx]+)\.\s(.+)$')

    headings = {}
    current_heading = None
    current_subheading = None

    for line in text.split('\n'):
        match = section_pattern.match(line)
        if match:
            # found a new section heading
            heading_num = match.group(1)
            heading_title = match.group(2)
            headings[heading_num] = {
                "title": heading_title,
                "subheadings": []
            }
            current_heading = heading_num
            current_subheading = None
        elif line.startswith('- '):
            # found a new subheading
            subheading_title = line[2:]
            if current_heading:
                headings[current_heading]["subheadings"].append(subheading_title)
                current_subheading = subheading_title


    # Write the dictionary to a JSON file
    with open('headings.json', 'w') as f:
        json.dump(headings, f, indent=2)

    print('JSON written to file "headings.json"')

    # Read the JSON file into a dictionary
    with open('headings.json', 'r') as f:
        headings = json.load(f)
    #     print(headings)

    # Traverse the dictionary and print the headings and subheadings
    for heading_num, heading_data in headings.items():
        print(f'{heading_num}. {heading_data["title"]}')
        for subheading in heading_data['subheadings']:
            print(f'- {subheading}')
            
        





    
    


# def insert_images_in_file(file_path, image_list):
#     """
#     Inserts an image URL from the given list before each level 2 (##) heading in the Markdown file
#     located at the given file path.
#     """
#     with open(file_path, "r") as f:
#         markdown = f.read()
# 
#     new_markdown = insert_images(markdown, image_list)
# 
#     with open(file_path, "w") as f:
#         f.write(new_markdown)


    # Make the REST API call to the WordPress API
#     response = requests.post('https://example.com/wp-json/wp/v2/posts', json=post_data, headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN'})
#     if response.status_code == 201:
#       print('Post created successfully')
#     else:
#       print('Error creating post')

# from bing_image_downloader import downloader
# # Call receive_data_chunk() function when each chunk of data is received
# receive_data_chunk({'field1': 'value1'})
# receive_data_chunk({'field2': 'value2'})
# receive_data_chunk({'field3': 'value3'})
# 
# # Call on_data_received() function when all data is received
# on_data_received()



################