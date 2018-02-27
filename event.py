
class Event:
    """Class with event information"""

    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    def __repr__(self):
        return '''
        Event Name: {}
        Date:       {}
        Location:   {}
        '''.format(self.name, self.date, self.location)