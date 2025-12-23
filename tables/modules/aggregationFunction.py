class aggregationFunction:
    @staticmethod
    def sum(column):
        akk = 0
        for x in column:
            akk += x
        return akk

    @staticmethod
    def count(column):
        return len(column)
