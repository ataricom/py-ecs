import abc
import random


class System:
    @abc.abstractmethod
    def update(self):
        pass


class Physics(System):
    def __init__(self):
        self.subscribers = []

    def update(self):
        for ent in self.subscribers:
            position = ent.get_component('Position')
            position.x += random.random() - 0.5
            position.y += random.random() - 0.5
            position.z += random.random() - 0.5
