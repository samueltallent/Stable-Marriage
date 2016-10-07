import copy


class Little(object):
    def __init__(self, name='', id=-420, ranking=[]):
        self.name    = name
        self.id      = id
        self.ranking = ranking
        self.engaged = False
        self.options = copy.deepcopy(ranking)
        self.fiance  = None

    def __repr__(self):
        return ' '.join([self.name, str(self.id), str(self.ranking), str(self.engaged)])
