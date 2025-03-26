class india():
    def capital(self):
        print("new delhi is the capital of india")
    def language(self):
        print("hindi is the most widely spoken language")
    def type(self):
        print("India is a developing country")
class usa():
    def capital(self):
        print("washington ,d.c is the capial of usa")
    def language(self):
        print("English is the most widely spoken language")
    def type(self):
        print("usa is a developed country")
obj_ind=india()
obj_usa=usa()

for country in(obj_ind,obj_usa):
 country.capital()
 country.language()
 country.type()