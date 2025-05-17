# DevOps Emgineer - Developer has an API 

import requests   # In terminal please do pip install requests 
demo_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url=demo_url)

#print(response) # Result <Response [200]>

#print(dir(response))

#print(response.json())  # Prints output in json format

#print(type(response.json())) # <class 'list'>


#print(response.json()[0])

def get_api_data():    ### Declare Function 
    demo_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=demo_url)    
    return response.json()

get_api_data() # Get data
