variable = 1

class Car:
    
    def __init__(self, my_var): 
        self.seat = my_var
        self.wheel = 2
 
 
class Frame():
    class Car(Car):
        def __init__(self):
            self.pedal = 3
    def __init__(self):
        self.car = Frame.Car()
           
    
test = Car(variable)
# print(test.__dict__)

frm = Frame()
# print(frm.car.__dict__)

print(test.seat is variable)
test.seat += 10
print(test.seat is variable)
print(test.seat)

