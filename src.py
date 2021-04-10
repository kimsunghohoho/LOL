from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"페이커,lol 너구리, 표식, 롤 데프트, 롤 메라","limit":50,"print_urls":True, "foramt": "jpg"}   #creating list of arguments
paths = response.download(arguments )   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images