#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print (r.status_code)
print(r.headers)

github_url = "https://raw.github.com/sewingpillows/labs/lab1/main.py"
r = requests.get(github_url)
print(r.text)
