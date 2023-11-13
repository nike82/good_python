class String:
    is_empty = False


s1 = String()
s2 = String()

s2.is_empty = True

print(s2.__dict__)
print(s1.__dict__)
print(String.__dict__)