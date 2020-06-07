import abc


class System:
    @abc.abstractmethod
    def update(self):
        pass


class Physics(System):
    def __init__(self):
        self.gravity = -9.81
        self.subscribers = []

    def update(self):
        for ent in self.subscribers:
            position = ent.get_component('Position')
            print(position)
            position.y += self.gravity
