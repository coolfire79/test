import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

r = requests.get('http://coolfire.uk.to', verify=False)
print(r.text)
