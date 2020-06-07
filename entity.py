class Entity:
    id = -1

    def __init__(self):
        self.id = self._set_id()
        self.components = dict()
        self.type = 'generic'

    def get_component(self, component):
        if component in self.components:
            return self.components.get(component)
        else:
            print('entity {} does not have component {}'.format(self.id, component))

    @classmethod
    def _set_id(cls):
        cls.id += 1
        return cls.id

