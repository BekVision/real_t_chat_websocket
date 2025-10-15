from abc import ABC, abstractmethod
class ToyABC(ABC):
    @abstractmethod
    def play(self):
        pass

class Car(ToyABC):
    def play(self):
        print('car play')

class Doll(ToyABC):
    def play(self):
        print('doll play')

TOY_VARIUS = {
    'car': Car(),
    'doll': Doll(),
}

class ToyFactory:
    @staticmethod
    def create_toy(toy, str):
        if toy not in TOY_VARIUS:
            raise ValueError("Unknown toy: ")
        return TOY_VARIUS[toy].play()

if __name__ == '__main__':
    toy = ToyFactory()
    toy.create_toy('Toy 1')
    toy.create_toy('Toy 2')
    toy.create_toy('Toy 3')