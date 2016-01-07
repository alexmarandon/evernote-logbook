from evernote.api.client import EvernoteClient
from evernote.api.client import NoteStore
import evernote.edam.type.ttypes as Types
import evernote.edam.error.ttypes as Errors
import json

fname = 'apikey.json'

str_data = open(fname).read()
apikey = json.loads(str_data)


# generate a new dev token:
# https://sandbox.evernote.com/api/DeveloperToken.action
dev_token = apikey['token']

client = EvernoteClient(token=dev_token)
uStore = client.get_user_store()
user = uStore.getUser()
print "Evernote User Name:", user.username
nStore = client.get_note_store()


tgname = raw_input('Enter a tag name: ')
ourTag = Types.Tag()
ourTag.name = tgname


try:
    tag = nStore.createTag(ourTag)
    print "Tag %s :: %s successfully created" % (tag.guid, tag.name)
except Errors.EDAMUserException, edue:
	##BAD_DATA_FORMAT "Tag.name" - invalid length or pattern
    ##BAD_DATA_FORMAT "Tag.parentGuid" - malformed GUID
    ##DATA_CONFLICT "Tag.name" - name already in use
    ##LIMIT_REACHED "Tag" - at max number of tags
	print "EDAMUserException:", edue
except Errors.EDAMNotFoundException, ednfe:
	## "Tag.parentGuid" - not found, by GUID
	print "EDAMNotFoundException: Tag.parentGuid not Found"

