import os

class FileHandler:

    def __init__():
        self.directory = os.expanduser('~') + './simple_backup'

        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def save (filename, data):
        f = open(filename, 'w')
        f.write(data)
        f.close()

    def load (filename):
        f = open(filename)
        data = f.read()
        f.close()
        return data
