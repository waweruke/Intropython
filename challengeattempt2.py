def filteredlist(mainlist):
    newlist = []
    for item in mainlist:
        if len(item) > 4 and len(item) < 7 :
            newlist.append(item)
        return newlist
mylist = ("reagan", "millicent", "emilly", "mark", "joseph", "maczuckerbug", "jamesbond", "abdallah", "bob")
filteredlist = filteredlist(mylist)
print(filteredlist)