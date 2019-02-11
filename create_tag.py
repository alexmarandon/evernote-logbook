from evernote.api.client import EvernoteClient
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


def makeTag(tagname):
    ourTag = Types.Tag()
    ourTag.name = tagname
    try:
        tag = nStore.createTag(ourTag)
        print "Tag %s :: %s successfully created" % (tag.guid, tag.name)
    except Errors.EDAMUserException, edue:
        ##BAD_DATA_FORMAT "Tag.name" - invalid length or pattern
        ##BAD_DATA_FORMAT "Tag.parentGuid" - malformed GUID
        ##DATA_CONFLICT "Tag.name" - name already in use
        ##LIMIT_REACHED "Tag" - at max number of tags
        print "EDAMUserException:", edue
        return None
    except Errors.EDAMNotFoundException, ednfe:
        ## "Tag.parentGuid" - not found, by GUID
        print "EDAMNotFoundException: Tag.parentGuid not Found"
        return None
    ## Return created tag object
    return tag


tgname = raw_input('Enter a tag name: ')
makeTag(tgname)

def makeWeekTags():
    i = 0
    while i<53:
        i+=1
        if i<10 : tgname = 'ww:0%s' % str(i)
        else : tgname = 'ww:%s' % str(i)
        makeTag(tgname)
    return None
    
def makeYearTags():
    
    makeTag('yy:2013')
    makeTag('yy:2014')
    makeTag('yy:2015')
    makeTag('yy:2016')
    return None
    
def makeMonthTags():
    
    makeTag('mm:january')
    makeTag('mm:february')
    makeTag('mm:march')
    makeTag('mm:april')
    makeTag('mm:may')
    makeTag('mm:june')
    makeTag('mm:july')
    makeTag('mm:august')
    makeTag('mm:september')
    makeTag('mm:october')
    makeTag('mm:november')
    makeTag('mm:december')
    return None
    
#makeWeekTags()
#makeMonthTags()
#makeYearTags() 
    