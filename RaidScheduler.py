import dbMethods

# create new raid event
def createRaidEvent(host, time, wings):
    role = "host"
    dbMethods.createTable_EventTable(host)
    dbMethods.addPlayer(host, host, role, time, wings)


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
def addToList():
    pass

# removes person from a raid event list
def RemoveFromList():
    pass

# officer must be able to schedule raid

#user must be able to react to message to sign up

#user must be able to un react to message to un sign up