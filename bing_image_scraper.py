import os
import shutil
from bing_image_downloader import downloader


def imagegenerator(keywords):
    
    keywords = keywords
    # Get the list of keywords as input
#     keywords = ['dog', 'cat']

    # Create the images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Create the images_all directory if it doesn't exist
    if not os.path.exists('images_all'):
        os.makedirs('images_all')

    # Iterate over keywords
    for keyword in keywords:
        # Download images using the keyword
        downloader.download(keyword, limit=2, output_dir='images')

    # Iterate over the directories in the images folder
    for directory in os.listdir('images'):
        # Iterate over the files in the directory
        for j, file_name in enumerate(os.listdir(os.path.join('images', directory))):
            # Construct the new file name
            new_file_name = directory + '_' + str(j + 1) + '.jpg'
            # Check if the new file name already exists in the images_all directory
            if os.path.exists(os.path.join('images_all', new_file_name)):
                # If it exists, delete the existing file before copying the new file
                os.remove(os.path.join('images_all', new_file_name))
            # Copy the file to the images_all folder
            shutil.copy(os.path.join('images', directory, file_name), os.path.join('images_all', new_file_name))







# import os
# from bing_image_downloader import downloader
# 
# # # Get the list of keywords as input
# # keywords = input("dog, cat, bird").split(',')
# keywords = ['dog', 'cat']
# 
# # Create the images directory if it doesn't exist
# if not os.path.exists('images'):
#     os.makedirs('images')
# # Create the images_all directory if it doesn't exist
# if not os.path.exists('images_all'):
#     os.makedirs('images_all')
# 
# # Iterate over keywords
# for i, keyword in enumerate(keywords):
#     # Download images using the keyword
#     downloader.download(keyword, limit=2, output_dir='images')
# 
# 
# # Iterate over the directories in the images folder
# for i, directory in enumerate(os.listdir('images')):
#     # Iterate over the files in the directory
#     for j, file_name in enumerate(os.listdir(os.path.join('images', directory))):
#         # Construct the new file name
#         new_file_name = directory + '_' + str(j + 1) + '.jpg'
#         # Move the file to the images_all folder
#         os.rename(os.path.join('images', directory, file_name), os.path.join('images_all', new_file_name))
# 