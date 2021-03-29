import dbMethods

# create new raid event
def createRaidEvent(host, time, wings):
    role = "host"
    dbMethods.createTable_EventTable(host)
    dbMethods.addPlayer(host, host, role, time, wings)

def deleteRaidEvent(host):
    dbMethods.deleteTable_EventTable(host)

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
def postRaid():
    pass

# adds person to a raid event list
def addToList(host, user):
    role = "player"
    time = "na"
    wings = "na"
    dbMethods.addPlayer(host, user, role, time, wings)

# removes person from a raid event list
def RemoveFromList(host, user):
    dbMethods.removePlayer(host, user)

# officer must be able to schedule raid

#user must be able to react to message to sign up

#user must be able to un react to message to un sign up