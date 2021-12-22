import dbMethods

# create new raid event
def createRaidEvent(host, hostID, messageID, channelID):
    role = "host"

    dbMethods.createTable_EventTable(hostID)
    dbMethods.createTable_InfoTable(hostID, messageID, channelID)

    dbMethods.addPlayer(hostID, host, role)

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
def addToList(hostID, user):
    role = "player"
    dbMethods.addPlayer(hostID, user, role)

# removes person from a raid event list
def removeFromList(host, user):
    dbMethods.removePlayer(host, user)
