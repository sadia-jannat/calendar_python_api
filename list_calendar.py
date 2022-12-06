from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE='client_secret_file.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

response=service.calendarList().list().execute()
pprint(response)

#keys print
print(response.keys())

#iteams print
print(response.get('items'))
#print(response.get('items')[0])