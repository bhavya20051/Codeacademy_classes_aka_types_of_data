#Function that checks if a list has the attribute count and then uses it to count amount of s's in the list
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in how_many_s:
  if hasattr(element,"count"):
    print(element.count("s"))