import json

fname = raw_input('Enter the Evernote API Key file name: ')
if ( len(fname) < 1 ) : fname = 'apikey2.json'

# {"key" : "evernote_username", 
# "secret" : "secret_key",
# "token" : "authentification token"}

str_data = open(fname).read()
apikey = json.loads(str_data)

key = apikey['key']
secret = apikey['secret']
token = apikey['token']

print key, secret, token

