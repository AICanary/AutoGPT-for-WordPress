import os
import subprocess
from CreatePost import PostGenerator
import shutil
# import upload_and_delete
# Define the name of the file to store the topics
filename = "topics.txt"



# ##########################################################
# 
# Open the input file
with open(filename, 'r') as input_file:
    # Read all the lines and remove empty lines
    lines = [line.strip() for line in input_file if line.strip()]

# Open the output file
with open('output_file.txt', 'w') as output_file:
    # Write the non-empty lines to the output file
    output_file.write('\n'.join(lines))
    # Read the topics as a list of strings, removing any whitespace or newlines
# Open the output file
with open('output_file.txt', 'r') as output_file:
    # Read all the lines and remove any whitespace characters
    topics = [line.strip() for line in output_file]

# # Traverse through the list and print each line
# for line in lines:
#     print(line)

    post_generators = []
    for topic in topics:
        post_generator = PostGenerator(topic)  # Create an instance of the PostGenerator class
        post_generators.append(post_generator)  # Add the instance to a list or other data structure
#     
# 
# ##################################################

subprocess.run(["python", "upload_and_delete.py"])



    

# Run the script.py file

    