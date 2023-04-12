
# 3 in one code

from easyscrape_googlesuggest import getsuggestions as ES

# Request suggestions for a search term
ESResults = ES.query("botox vs")
print(ESResults)




###################################

# 
# import suggests
# s = suggests.get_suggests('warts ', source='google')
# print(s)
# 
# tree = suggests.get_suggests_tree('abortion', source='google', max_depth=1)
# print(tree)
# 
# 
# edges = suggests.to_edgelist(tree)
# 
# edges.head()
# 
# edges = suggests.add_parent_nodes(edges)
# edges = edges.apply(suggests.add_metanodes, axis=1)
# show_cols = ['source','target','grandparent','parent','source_add','target_add']
# edges[show_cols].head()
# 
# 
# 
# 
# 
# #############################
# 
# 
# from google_trends import daily_trends, realtime_trends
# today_trends =daily_trends(date=None, country='PK', language='en-US', timezone='+300')
# print(today_trends)
# # trends today
# today_trends = daily_trends(country="PK")
# print(today_trends)
# 
