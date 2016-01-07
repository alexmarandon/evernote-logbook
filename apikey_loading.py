import json

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'apikey.json'

# {"key" : "evernote_username", 
# "secret" : "secret_key"}

str_data = open(fname).read()
apikey = json.loads(str_data)

key = apikey["key"]
secret = apikey["secret"]

print key, secret

