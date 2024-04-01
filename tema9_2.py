class Tomato:
    # 2) Статическое свойство со стадиями созревания помидора
    states = {
        'отсутствует': 0,
        'цветение': 1,
        'зеленый': 2,
        'красный': 3
    }
    
    def __init__(self, index):
        # 3) Динамические свойства:
        #    _index - индекс помидора
        #    _state - стадия созревания (принимает первое значение из словаря states)
        self._index = index
        self._state = list(self.states.keys())[0]  # Начальная стадия - "отсутствует"

    def grow(self):
        # 4) Метод для перехода на следующую стадию созревания
        if self._state != list(self.states.keys())[-1]:
            current_index = list(self.states.keys()).index(self._state)
            self._state = list(self.states.keys())[current_index + 1]

    def is_ripe(self):
        # 5) Метод для проверки, что томат созрел
        return self._state == 'красный'


class TomatoBush:
    def __init__(self, num):
        # 2) Динамическое свойство tomatoes - список объектов класса Tomato
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        # 3) Метод для перевода всех томатов на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # 4) Метод для проверки, все ли томаты созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        # 5) Метод для сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        # 2) Динамические свойства:
        #    name - имя садовника (передается параметром, является публичным)
        #    _plant - объект класса TomatoBush
        self.name = name
        self._plant = plant

    def work(self):
        # 3) Метод для ухода за растением
        self._plant.grow_all()

    def harvest(self):
        # 4) Метод для сбора урожая
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Пока не все помидоры созрели. Продолжайте ухаживать за растением.")

    @staticmethod
    def knowledge_base():
        # 5) Статический метод для вывода справки по садоводству
        print("Справка по садоводству:")
        print("1. Помидоры проходят через несколько стадий созревания: отсутствует, цветение, зеленый, красный.")
        print("2. Садовник должен следить за ростом и созреванием помидоров.")
        print("3. Собирать урожай можно только после полного созревания всех помидоров на кусте.")


# Тесты

# 2) Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener("Иван", bush)


