from evernote.api.client import EvernoteClient
from evernote.api.client import NoteStore
import json
from libevnt import getDictLogNotebooks, getStrgNotebookGUID

fname = 'apikey2.json'
apikey = json.loads(open(fname).read())
dev_token = apikey['token']


client = EvernoteClient(token=dev_token, sandbox=False)
uStore = client.get_user_store()
user = uStore.getUser()
print "Evernote User Name:", user

nStore = client.get_note_store()

dNotebooks = getDictLogNotebooks(nStore)
print dNotebooks["Logbook_2019"]
print getStrgNotebookGUID(nStore, "Logbook_2018")

