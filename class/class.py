# import random
# class Character:
#     def __init__(self, name, hp, atk, spd):
#         self.name = name 
#         self.atk = atk 
#         self.hp = hp 
#         self.spd = spd 
    
#     def atk(self):
#         print(f'attack {self.name}')
    
#     def atkBy(self, opponent):
#         print(f'attack by {self.name}')
        
#     def getHp(self):
#         get_hp = random.randint(0,100)
#         total_hp = self.hp + get_hp
#         print(f'get {get_hp} hp')
#         print(f'total hp = {total_hp}')
    
# rudi = Character("rudi", 100, 5, 10)
# ambaritron = Character("ambaritron", 100, 5, 10)

# rudi.atkBy(ambaritron)
# ambaritron.atkBy(rudi)

# rudi.getHp()

# class Utilitas:
#     @staticmethod
#     def tambah(x, y):
#         return x + y

# # Menggunakan metode statis
# hasil = Utilitas.tambah(5, 3)
# print(f"Jumlah: {hasil}")

# Python program to explain property()
# function using decorator

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Usia tidak boleh negatif")
        self._age = value

person1 = Person(30)
print(person1.age)
person1.age = 0
print(person1.age)