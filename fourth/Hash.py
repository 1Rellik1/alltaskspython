class Hash:
    def __init__(self):
        self._d = {}

    def __getitem__(self, key):
        h = self.__get_hash(key)
        return self._d.__getitem__(h)

    def __setitem__(self, key, value):
        h = self.__get_hash(key)
        self._d.update({h: value})

    def __get_hash(self, name):
        return hash(name)

# 104
# [None, None, None, 248, 142, 104, 215, None, None, 59, 101, None, None, 152, None, None, None, None, 95, None]
