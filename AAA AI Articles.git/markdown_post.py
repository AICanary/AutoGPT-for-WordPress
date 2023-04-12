
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
# print(openai_API)
# print(username)
# print(pythonapp)
# print(password)
# print(domain_name)
# print(phone)


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