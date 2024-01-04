import requests
from datetime import datetime
USERNAME='amber1995'
TOKEN="aof8318nfda8dnaf038"
GRAPHID="graph45"
pixela_endpoint="https://pixe.la/v1/users"

#FIRST: CREATE A USER ACCOUNT
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
#THEN: CREATE A GRAPH
graph_config={
    "id":GRAPHID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN": TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today=datetime.now()
prev_date=datetime(year=2022,month=1,day=9).strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))
pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you cycled today?")
}

# response=requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)
#
# put_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{prev_date}"
# put_params={
#     "quantity":"17.8"
# }

# response=requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{prev_date}"

response=requests.delete(url=delete_endpoint, headers=headers)
print(response.text)