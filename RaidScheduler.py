import dbMethods

# create new raid event
def createRaidEvent(host, time, wings):
    role = "host"
    dbMethods.createTable_EventTable(host)
    dbMethods.createTable_InfoTable(host)
    dbMethods.addPlayer(host, host, role)

def deleteRaidEvent(host):
    dbMethods.deleteTable_EventTable(host)
    dbMethods.deleteTable_InfoTable(host)

# check to see if raid event already exists
def checkRaid(host):
    # if table already exists with this users name, then return true
    # else return false
    ifTableExists = dbMethods.checkTable(host)
    if ifTableExists:
        return True
    else:
        return False

# posts raid event information into the text chat
def postRaid(host):
    return dbMethods.readTable(host)

# adds person to a raid event list
def addToList(host, user):
    role = "player"
    dbMethods.addPlayer(host, user, role)

# removes person from a raid event list
def removeFromList(host, user):
    dbMethods.removePlayer(host, user)

# officer must be able to schedule raid

#user must be able to react to message to sign up

#user must be able to un react to message to un sign up