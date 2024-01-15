import requests

Response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
 
complete_details = Response.json()

for elements in range(len(complete_details)):
  print(complete_details[elements]["user"]["login"])
