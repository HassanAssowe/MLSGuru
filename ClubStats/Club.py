class Club:
    def __init__(self, id, fullName, shortName, abbr):
        self.id = id
        self.fullName = fullName
        self.shortName = shortName
        self.abbr = abbr


    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self, value):
        self.id = value
        
    @property
    def fullName(self):
        return self.fullName
    
    @fullName.setter
    def fullName(self, value):
        self.fullName = value

    @property
    def shortName(self):
        return self.shortName
    
    @shortName.setter
    def shortName(self, value):
        self.shortName = value
    
    @property
    def abbr(self):
        return self.abbr
    
    @abbr.setter
    def abbr(self, value):
        self.abbr = value