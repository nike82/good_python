import sys


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for item in data:
            self.lst_data.append(dict(zip(self.FIELDS, item.split())))


    def select(self, a, b):
        return self.lst_data[a:b+1]


lst_in = ["1 Mark 35 12000", "2 John 44 12000", "3 Greg 23 1900"]

db = DataBase()
db.insert(lst_in)
print(db.lst_data)
