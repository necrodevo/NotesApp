import requests

URL = "http://127.0.0.1:8000"

REQUEST = requests.get(URL)

STATUS = REQUEST.raise_for_status
#returning data
data = REQUEST.text
print(REQUEST.status_code,REQUEST.text)
 