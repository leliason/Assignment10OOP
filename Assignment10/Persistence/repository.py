class Repository:

    def __init__(self):
        self._records = []

    def save(self, record):
        self._records.append(record)

    def get_all(self):
        return self._records