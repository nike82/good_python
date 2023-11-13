class Translator:
    def add(self, eng, rus):
        if "dictionary" not in self.__dict__:
            self.dictionary = {}
        self.dictionary.setdefault(eng, [])
        if rus not in self.dictionary[eng]:
            self.dictionary[eng].append(rus)

    def remove(self, eng):
        self.dictionary.pop(eng, False)


    def translate(self, eng):
        return self.dictionary[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")

print(tr.translate("car"))
tr.add("car", "тачка")
print(tr.translate("car"))
