class Read_File(object):
    def receiv_name(self, name):
        self.name = name

    def read(self):
        return open(self.name).readlines()