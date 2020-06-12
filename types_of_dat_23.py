#function that overwrites the append function  and automatically sorts a list after the asppending of a value
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()