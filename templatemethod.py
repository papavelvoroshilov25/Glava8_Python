from __future__ import annotations
from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):

    def prepareRecipe(self) -> None:
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    def boilWater(self) -> None:
        print('Кипятим воду')

    def pourInCup(self) -> None:
        print('Переливаем в чашку')

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def addCondiments(self) -> None:
        pass

    def customerWantsCondiments(self) -> bool:
        return True

class Tea(CaffeineBeverage):

    def brew(self) -> None:
        print('Завариваем чай')

    def addCondiments(self) -> None:
        print('Добавляем лимон')

    def customerWantsCondiments(self) -> bool:
        print('Хотите добавить лимон в чай (д/н)?')
        answer = input()
        if answer.lower().startwith('д'):
            return True
        else:
            return False

class Coffee(CaffeineBeverage):

    def brew(self) -> None:
        print('Пропускаем кофе через фильтр')

    def addCondiments(self) -> None:
        print('Добавляем сахар и молоко')

    def customerWantsCondiments(self) -> bool:
        print('Хотите добавить молоко и сахар в кофе (д/н)?')
        answer = input()
        if answer.lower().startwith('д'):
            return True
        else:
            return False

if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print('Готовим чай...')
    tea.prepareRecipe()
    print()

    print('Готовим кофе...')
    coffee.prepareRecipe()





