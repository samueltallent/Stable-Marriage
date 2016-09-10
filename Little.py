class Little(object):
    def __init__(self, name='', id=-420, ranking=[]):
        self.name = name
        self.id   = id
        self.ranking = ranking
        self.engaged = False

    def __repr__(self):
        return ' '.join([self.name, str(self.id), str(self.ranking), str(self.engaged)])

    def calculatePreferences(self, options):
        pass