from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE='client_secret_file.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

#request_body={
#   'summary':'calendar event'}

#to delete calendar
service.calendars().delete(calendarId='8l3v0tc3hbhg145agifhfgip7s@group.calendar.google.com').execute()
