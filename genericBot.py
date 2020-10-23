def searchRoles(roleList, search):

    for item in roleList:
        if item.name == search:
            searchResult = item
            return searchResult