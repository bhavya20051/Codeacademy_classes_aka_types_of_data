#You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. 
# The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.
#First, we need to create menus and describe their times available by organizing them in class Menu
#Then, we need to keep track of franchises in a business which we do using class Franchise
#Finally we need to create a new business by first creating menus and a franchise before finally creating a business using class Business
class Menu:
  
  

  def __init__(self, name, items, start_time, end_time):
       self.name=name
       self.items=items
       self.start_time=start_time
       self.end_time=end_time
       
  def __repr__(self):
    return ("{} menu available from {}:00 to {}:00").format(self.name,self.start_time,self.end_time)
  def calculate_bill(self,purchased_items):
    bill=0
    for item in purchased_items:
      if item in self.items:
        bill+=self.items[item]
    return bill

brunch= Menu("brunch",{ 
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50 , 'orange juice': 3.50
  }, 11, 16)

print(brunch)

early_bird= Menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
  }, 15, 18 )

print(early_bird)

dinner= Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattra formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23 )

print(dinner)

kids= Menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

print(kids)
print(brunch.calculate_bill(["pancakes","home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate","mushroom ravioli (vegan)" ]))

class Franchise:
  def __init__(self,address,menus):
    self.address=address
    self.menus=menus
  def __repr__(self):
    return("The address of the restaurant is {}".format (self.address))
  def available_menus(self,time):
    self.time=time
    available=[]
    for menu in self.menus:
      if menu.start_time <= self.time <= menu.end_time:
        available.append(menu)
    return available
    


flagship_store= Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment= Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

print(flagship_store)
print(new_installment)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

class Business:
  
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
  def __repr__(self):
    return "This is {}".format(self.name)
Biz_1= Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])

arepas_menu= Menu("arepas menu", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20 )


arepas_place= Franchise("189 Fitzgerald Avenue",arepas_menu)
Biz_2= Business("Take a' Arepa", arepas_place)