# Overview on Python strip, lstrip (left), and rstrip (right) Functions

url = 'https://google.com'

# print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)

