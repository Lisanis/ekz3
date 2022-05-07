class Tomato:
    # Cтадии созревания помидора
    states = ['unripe', 'ripe', 'overripe']

    def __init__(self, index, state=states[0]):
        self._index = index
        self._state = state

    # Переход к следующей стадии созревания
    def grow(self):
        self._index += 1
        self._state = self.states[self._index]

    # Проверяем созрел ли томат
    def is_ripe(self):
        if self._state == 'overripe':
            print('Your tomato is ripe')
            return True
        else:
            print('Your tomato is not ripe')
            return False


class TomatoBush:

    # Создаём спсок из объектов класса Tomato
    def __init__(self, coutn):
        self.tomatoes = [Tomato(0) for index in range(0, coutn)]

    # Переводим все томаты на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Работа садовника
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    # Сбор урожая
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is not ripe.')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''The collection of tomatoes must be carried out, 
    observing the ripening dates, and the first tomatoes in the 
    greenhouse are harvested at the stage of full maturity.''')


# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

Gardener.knowledge_base()
tomato_bush_1 = TomatoBush(5)
gardener = Gardener('Emilio', tomato_bush_1)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
