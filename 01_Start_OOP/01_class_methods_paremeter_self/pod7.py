import sys


# class StreamData:
#     def create(self, fields, lst_values):
#         if len(lst_values) == len(fields):
#             setattr(self, fields[0], lst_values[0])
#             setattr(self, fields[1], lst_values[1])
#             setattr(self, fields[2], lst_values[2])
#             return True
#         return False

class StreamData:
    def create(self, fields, lst_values):
        if len(lst_values) == len(fields):
            for index, key in enumerate(fields):
                setattr(self, fields[key], lst_values[index])
            return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')
    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

