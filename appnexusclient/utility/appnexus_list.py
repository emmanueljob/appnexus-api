

class AppnexusList(list):
    _count = 0

    def count(self):
        return self._count

    def set_count(self, count):
        self._count = count

    def __len__(self):
        return self._count
