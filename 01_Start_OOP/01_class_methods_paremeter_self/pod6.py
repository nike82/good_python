
class Stepik:
    def next_task(self):
        return "Следующее задание"


my_st = Stepik()
print(Stepik.next_task(my_st))
print(my_st.next_task())

