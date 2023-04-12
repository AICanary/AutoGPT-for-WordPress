from duckduckgo_search import ddg_images

keywords = 'hydrafacial'
# r = ddg_images(keywords=keywords, region='br-pt', safesearch='Off', time='Year', size='Wallpaper', 
#                color='Green', type_image='Photo', max_results=100,  download=True,)

r = ddg_images(keywords=keywords, max_results=300,  download=True,)
print(r)