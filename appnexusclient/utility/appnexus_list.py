

class AppnexusList(list):
    count = 0

    def count(self):
        return self.count

    def set_count(self, count):
        self.count = count

    def __len__(self):
        return self.count
