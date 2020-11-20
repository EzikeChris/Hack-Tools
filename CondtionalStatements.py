#IF ELSE SCENARIO


def drink(money)
      if money >= 2:
          return 'Your Drink is Served'
          else:
              return 'No Drink Served'

print (drink(3))
print(drink(1))


def alcohol(age,money)
           if (age >= 21 ) and (money >= 5):
               return 'we re getting a drink'
            else (age >= 21) and (money < 5):
               return 'come back with more money.'
               else (age < 21) and (money >= 5)
                 return 'Fuck Uoff'
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))      