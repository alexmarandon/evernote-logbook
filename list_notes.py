from evernote.api.client import EvernoteClient
from evernote.api.client import NoteStore
import json

fname = 'apikey2.json'

str_data = open(fname).read()
apikey = json.loads(str_data)

nbname = raw_input('Enter the Evernote NoteBook: ')
if ( len(nbname) < 1 ) : nbname = 'logbook_2015'


# generate a new dev token:
# https://sandbox.evernote.com/api/DeveloperToken.action
dev_token = apikey['token']


client = EvernoteClient(token=dev_token, sandbox=False)
uStore = client.get_user_store()
user = uStore.getUser()
print "Evernote User Name:", user.username


nStore = client.get_note_store()

notebooks = nStore.listNotebooks()
nbexists=False
for n in notebooks:
    if (n.name==nbname): 
        nbexists=True
        nbguid = n.guid
        print 'Notebook %s found, guid:%s' % (nbname, nbguid)
if not(nbexists): print 'Notebook %s has not been found' % nbname


filter = NoteStore.NoteFilter()
filter.order = 5
filter.ascending = True
if (nbexists): filter.notebookGuid = nbguid

spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
spec.includeTagGuids = True

ourNoteList = nStore.findNotesMetadata(filter, 0, 100, spec)

for note in ourNoteList.notes:
    print "%s :: %s" % (note.guid, note.title)
    #print note.tagGuids