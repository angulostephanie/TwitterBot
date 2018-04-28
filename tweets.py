from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import tweepy, time, sys

CONSUMER_KEY = keys.consumer_key
CONSUMER_SECRET = keys.consumer_secret
ACCESS_KEY = keys.access_token
ACCESS_SECRET = keys.access_token_secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# access google sheets
#

def retweet(id):
    # example - 990335296129527808 (need to parse the link and get the number)
    tweet = api.get_status(id)
    tweet.retweet()


# how to post tweets

api.update_status("This is a test!")



# sheets stuff
# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms' # TODO: change
RANGE_NAME = 'Class Data!A2:E'  # TODO: change
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))

