from google_images_search import GoogleImagesSearch

downloaded = []
def image_look(name):
    if name not in downloaded:
        # you can provide API key and CX using arguments,
        # or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
        gis = GoogleImagesSearch('AIzaSyB5hUEw9C4qGgrNmm0QBKPyOIZuTJSC2Bg', '47273cb0e5fa64986')

        # define search params
        # option for commonly used search param are shown below for easy reference.
        # For param marked with '##':
        #   - Multiselect is currently not feasible. Choose ONE option only
        #   - This param can also be omitted from _search_params if you do not wish to define any value
        _search_params = {
            'q': name,
            'num': 1,
            'fileType': 'jpg',
           # 'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
           # 'safe': 'active|high|medium|off|safeUndefined',  ##
           # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined',  ##
           # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined',  ##
           # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined',
            ##
           # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined'  ##
        }

        # this will only search for images:
        #gis.search(search_params=_search_params)

        # this will search and download:
        #gis.search(search_params=_search_params, path_to_dir='/path/')

        # this will search, download and resize:
        gis.search(search_params=_search_params, path_to_dir='G:\skincare-recommender\images', width=300, height=300, custom_image_name=name)
        downloaded.append(name)

    # search first, then download and resize afterwards:
    #gis.search(search_params=_search_params)
    #for image in gis.results():
    #   image.url  # image direct url
    #   image.referrer_url  # image referrer url (source)

    #    image.download('/path/')  # download image
    #    image.resize(500, 500)  # resize downloaded image

     #   image.path  # downloaded local file path
    path='images\\'+name+'.jpg'
    return path

#image_look('haha emoji')