# import urllib.request,json
# from .models import Source



# #source url as a variable
# source_url = None

# def configure_request(app):

#     global source_url
#     source_url = app.config['NEWS_SOURCES_URL']
#     print(source_url)


# def get_source():
#     get_source_url = source_url
#     print (get_source_url)

#     with urllib.request.urlopen(get_source_url)as url:
#         get_source_data = url.read()
#         get_source_response = json.loads(get_source_data)

#         source_results = None
#         if get_source_response['sources']:
#             source_results_list = get_source_response['sources']
#             source_results = process_results(source_results_list)

#     return source_results

# def process_results(source_list):
#     source_results = []
#     for source in source_list:
        
#         author = source.get('author')
#         quote = source.get('quote')
        

#         if author:

#             source_object =  Source(author,quote)
#             source_results.append(source_object)

#     return source_results