# -*- coding: utf-8 -*-
"""
Spyder Editor

In this script file, I created get and post requests with python.

Overview of HTTP:
    
    When you, the CLIENT, use a web page your browser sends an HTTP request 
    to the server where the page is hosted. The server tries to find the 
    desired resource by default "index.html". 
    If your request is successful, the server will send the object to the 
    client in an HTTP RESPONSE. This includes information like the type 
    of the RESOURCE, the length of the RESOURCE, and other information.
    The process can be broken into the request and response process. 
    The Request header passes additional information with an HTTP request.
    When an HTTP request is made, an HTTP method is sent, this tells 
    the server what action to perform like GET, POST, PUT, DELETE.
    The response header contains useful information. 
    Finally, we have the response body containing the requested file, 
    an  HTML  document. 
    
    Uniform resource locator (URL) is the most popular way to find resources 
    on the web. We can break the URL into three parts.

        - scheme this is this protocol, for this lab it will always be http://
        - Internet address or Base URL this will be used to find the location 
        here are some examples: www.ibm.com and  www.gitlab.com 
        - route location on the web server for example: /images/IDSNlogo.png
        
    You may also hear the term Uniform Resource Identifier (URI), 
    URL are actually a subset of URIs. Another popular term is endpoint, 
    this is the URL of an operation provided by a Web server.
    
"""

# REQUEST IN PYTHON

import requests

import os
from PIL import Image
from IPython.display import IFrame

# %% Get request

url = 'https://www.ibm.com/'

r = requests.get(url)   # get method

print(r.status_code) # a status code (200) meaning success

print("Request header: ", r.request.headers)

print("Request body: ", r.request.body)

# You can view the HTTP response header using the attribute headers. 
# This returns a python dictionary of HTTP response headers.

print(r.headers) 

# We can obtain the date the request was sent using the key Date

header = r.headers
print(header["Date"])

# Content-Type indicates the type of data:

print(header["Content-Type"])

print(r.encoding)

print(r.text[:100])

# You can load other types of data for non-text requests, like images

url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'

r = requests.get(url)
print(r.headers)
print(r.headers["Content-Type"])

# An image is a response object that contains the image as a bytes-like object
# As a result, we must save it using a file object

path = os.path.join(os.getcwd(), 'image.png')
print(path)

# We save the file, in order to access the body of the response 
# we use the attribute content then save it using the open function 
# and write method:

with open(path, 'wb') as f:
    f.write(r.content)
    
# We can view the image:
    
Image.open(path)

# %% Get request with URL parameters

""" 
You can use the GET method to modify the results of your query, 
for example retrieving data from an API. We send a GET request to the server. 
Like before we have the Base URL, in the Route we append /get, 
this indicates we would like to preform a GET request.

http://httpbin.org/get?Name=Joseph&ID=123

    - Name and ID are the parameter names
    - Joseph and 123 are the values of the parameters

"""



# The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service.

url_get = 'http://httpbin.org/get'

payload = {'Name':'Joseph', 'ID':'123'}

# Passing the dictionary payload to the params parameter of the  get() function:
r = requests.get(url_get,params=payload)

print(r.url)

print('Request body: ', r.request.body)

print(r.status_code)

print(r.text)

print(r.headers['Content-Type'])

# As the content 'Content-Type' is in the JSON format we can use the method json(), 
# it returns a Python dict:

print(r.json())

print(r.json()['args'])

# %% Post Request

"""
Like a GET request, a POST is used to send data to a server, 
but the POST request sends the data in a request body. 
In order to send the Post Request in Python, 
in the URL we change the route to POST. This endpoint will expect data 
as a file or as a form. A form is convenient way to configure 
an HTTP request to send data to a server.
"""

url_post = 'http://httpbin.org/post'

r_post = requests.post(url_post,data=payload)

print(r_post.status_code)

print('POST request url: ', r_post.url)
print('GET request url: ', r.url)

print('POST request body: ', r_post.request.body)
print('GET request body: ', r.request.body)

print(r_post.json()['form'])





