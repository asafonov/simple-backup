import os

class FileHandler:

    def __init__(self):
        self.directory = os.path.expanduser('~') + '/.simple_backup'

        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def save (self, filename, data):
        f = open(self.directory + '/' + filename, 'w')
        f.write(data)
        f.close()

    def load (self, filename):
        f = open(self.directory + '/' + filename)
        data = f.read()
        f.close()
        return data
