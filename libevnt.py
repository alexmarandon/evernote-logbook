from evernote.api.client import NoteStore

def getDictLogNotebooks(nStore):
    notebooks = nStore.listNotebooks()
    dNotebooks = {}
    for n in notebooks:
        if n.stack=="Logbooks":
        #if n.name[0:8]=="Logbook_":
            dNotebooks[n.name] = n.guid
            #print n.name, n.guid
    return dNotebooks

def getStrgNotebookGUID(nStore, logbookname):
    notebooks = nStore.listNotebooks()
    for n in notebooks:
        if n.name==logbookname:
            return n.guid
            break
    return False