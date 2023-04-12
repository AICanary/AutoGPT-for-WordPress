from pytrends.request import TrendReq

# create pytrends object
pytrends = TrendReq()

# set up search parameters
keyword = 'acne'
# related_topics = pytrends.related_topics()
# india_trends = pytrends.realtime_trending_searches(pn='IN') # India
#suggestions = pytrends.suggestions(keyword)

# print the data
# create pytrends object

# set up search parameters
search = pytrends.build_payload(kw_list=['acne'], geo='PK')

# get top trends in Pakistan
# top_trends_df = pytrends.top_charts(2023, hl='en-PK', tz=300, geo='PK')

# print the data
print(search)


#print(trends)
