install for mac
python and pip
brew install python
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
---------------
in wordpress go to user and create a new application password. name the application anyhing. it doesn't matter its for your efence. 

the password will be put in pythonapp in  configuration file config.ini

get the openai api key from te open ai account by going to settings and generating new openai key
replace in openai_API in config

username  is username of admin

password is not required but in case if something breaks you can try admin password here

domain name is you domain name with slash included example: https://example.pk/

phone number is the number where you want to whatapp the links too


example (note no qoutation marks):
[DEFAULT]
openai_API: sk-kfbgRHHmzN0t81GWcClzT3BlbkFg3WXXx4uFbYD7ryDComZ6
username = infoooskin
pythonapp = WbLU BccK vXLk ZEys cYVX 3Knw
password = *********
domain_name= https://example.pk/
phone: 03225155870


-------------------------
in wordpress


A- download file manager plugin
go to wp_content folder
go to plugins folder
and copy paste the folder 
WP_REST_API_Markdown_Update


B- install AIOSEO REST premium plugin

c- install WP Githuber MD and do settings that suits you. it will work with the default too. 


----------------

install thony
then run 

pip install requirements

you may get errors first time as its not tested for requirements yet on other system

----------------------
two step process
1. put the topics you want to write article about in topics.txt. you can copy the table from ahref and paste in here
2. run the TopicToPosts.py by clicking run in thony
3. once article is generated go to markdown_articles latest topic name (one with highest index number). in it 
a. see the article to be posted text to finalize it
b. go to images_all folder and delete any images not good for article. drag featured image in featured folder.
4. run upoad_and_delet.py folder


note: delete the folders which are uploaded from the markdown_articles folder or they will be uploaded again
----------------

note:
uploaded urls will be added to urls .txt file 
whatsapp data will be in PyWhatKit_DB
output will have topics for articles