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
print(phone)
print(Pexel_API)
print(Unsplash_Access_Key)
print(pexel_images)
print(Unsplash_images)
print(Catagories)

