class Unit():  # базовый класс

    count = 0 # глобальная переменная в классе

    def __init__(self, health, damage):  # конструктор базового класса c атрибутами
        self.health = health
        self.damage = damage
        Unit.count += 1 # обращение к глобальной переменной

    def get_unit_info(self): # self хранит все данные из кода выше
        return f'Здоровье: {self.health}; Урон: {self.damage};'

unit_1 = Unit(100, 5) # создание экземпляра класса
print(unit_1.get_unit_info()) # Здоровье: 100; Урон: 5;
print(Unit.count) # 1

class Human(Unit): # класс наследник

    def __init__(self, health, damage, type, armor):
        super(Human, self).__init__(health, damage) # наследование атрибутов
        #Unit.__init__(self, health, damage) # вариант 2 # если хоим указать конкретного родителя
        self.type = type
        self.armor = armor
    
    def get_unit_info(self): # переопределение метода базового класса
        return f'Здоровье: {self.health}; Урон: {self.damage}; Тип: {self.type}; Броня: {self.armor};'

human_1 = Human(100, 10, 'Воин', 15)
print(human_1.get_unit_info())# использование метода базового класса 
                              # Здоровье: 100; Урон: 10; Тип: Воин; Броня: 15;


