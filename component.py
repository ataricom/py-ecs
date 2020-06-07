import abc


class Component:
    @abc.abstractmethod
    def __str__(self):
        pass


class Position(Component):
    system = 'system.Physics()'

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x= {self.x}\ny= {self.y}\nz= {self.z}\n'
