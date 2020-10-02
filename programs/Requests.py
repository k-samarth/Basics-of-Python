import requests

# GET Method
re = requests.get('https://httpbin.org/get')
print (re.text) # will output the response from the "GET" method

# POST Method
re = requests.post('https://httpbin.org/post', data={'text': 'Hello World'})
print (re.text) # will output the response from the "POST" method
