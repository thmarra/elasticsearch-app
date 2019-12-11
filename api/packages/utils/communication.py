class Communication(object):

    def __init__(self, file=None, tags=[], owner=None, category=None):
        self.file = file
        self.tags = tags
        self.owner = owner,
        self.category = category

    def __validate(self, data):
        if 'file' not in data or data['file'] is not

    def insert(self, data):
        self.__validate(data)
