from Little import Little

def allLittlesMatched(littlesList):
    for little in littlesList:
        # print "Little: %s" % little.name
        print 'Little (%s) Engaged: %s' % (little.name, little.engaged)
        if not little.engaged:
            return False
    return True

def calculatePreferences(littles, bigs):
