import copy


class Big(object):
    def __init__(self, name='', id=-420, ranking=[]):
        self.name    = name
        self.id      = id
        self.ranking = ranking ## This is the list of options and their ranking, not meant to be modified
        self.engaged = False
        self.options = copy.deepcopy(ranking) ## This is the list of options, meant to be modified as algorithm progresses
        self.fiance  = None

    def __repr__(self):
        return ' '.join([self.name, str(self.id), str(self.ranking)])


    #This method assumes that the big calling this method is already engaged
    def prefers(self, other_little):
        if self.engaged:
            if self.fiance.id != other_little.id:
                if self.ranking.index(self.fiance.id) < self.ranking.index(other_little.id):
                    print "%s does not prefer the new potential little [%s] to their current little [%s], not switching" % (self.name, other_little.name, self.fiance.name)
                    return False
                print "%s prefers their new little [%s] to their current little [%s], switching" % (self.name, other_little.name, self.fiance.name)
                return True
            else:
                return False
        else:
            print "You must have called this method in error, %s is not yet engaged" % self.name