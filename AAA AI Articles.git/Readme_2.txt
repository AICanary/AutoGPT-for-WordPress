Steps to follow for the given instructions are as follows:

Instructions for WordPress:

1. Download the "File Manager" plugin in WordPress.
2. Navigate to the "wp_content" folder in WordPress and open the "plugins" folder.
3. Copy and paste the "WP_REST_API_Markdown_Update" folder here.
4. Install the "AIOSEO REST Premium" plugin.
5. Install the "WP Githuber MD" plugin and customize the settings as per your preference.

Instructions for Python:

1. Install "Thony" on your system.
2. Run the command "pip install requirements" in the Thony terminal. If there are errors, do not worry, it is because it has not been tested for requirements on another system.

Instructions for generating articles:

1. Put the desired topics to write about in a file named "topics.txt". You can copy the table from Ahrefs and paste it here.
2. Run "TopicToPosts.py" by clicking "Run" in Thony.
3. After the article is generated, go to the "markdown_articles" folder and find the latest topic name (the one with the highest index number).
4. In the folder, finalize the article text and delete any images that are not relevant to the article. Move the featured image to the "featured" folder.
5. Run the "upload_and_delete.py" file.

Note:

1. Delete the folders that have been uploaded from the "markdown_articles" folder, or they will be uploaded again.
2. The uploaded URLs will be added to the "urls.txt" file.
3. The WhatsApp data will be in the "PyWhatKit_DB".
4. The output will have topics for articles.

Instructions for OpenAI:

1. Go to the OpenAI account and click on "Settings".
2. Generate a new OpenAI API key.
3. Replace the "openai_API" in the configuration file "config.ini" with the newly generated API key.
4. Set the username as the username of the admin.
5. The password is not required, but you can use the admin password in case something breaks.
6. The domain name should be your domain name with a slash included, for example, "https://example.pk/".
7. The phone number is the number where you want to receive the links on WhatsApp.

Note: The application password can be created in WordPress by going to "User" and creating a new password. The name of the application can be anything, and it does not matter for your defense. The password should be put in "pythonapp" in the configuration file "config.ini".