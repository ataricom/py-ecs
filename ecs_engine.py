import entity
import component
import system


class EventManager:
    '''
    class EventManager
    Components
    Events have the format
    EventManager.send(sender, recipient, action)
    '''
    event_queue = []

    def message_send(self, sender, recipient, action):
        self.event_queue.append({'from': sender, 'to': recipient, 'action': action})


class EntityManager:
    entity_pool = dict()

    @classmethod
    def entity_add(cls):
        cls.entity_pool[entity.Entity.id] = entity.Entity()

    @classmethod
    def entity_remove(cls, entity_id):
        cls.entity_pool.pop(entity_id)

    @classmethod
    def entity_get(cls, entity_id):
        return cls.entity_pool.get(entity_id)

    @classmethod
    def component_add(cls, entity_id, comp):
        ent = cls.entity_get(entity_id)
        component_object = eval('component.' + comp)
        if comp not in ent.components:
            ent.components[comp] = component_object()
            sys = eval(component_object.system)
            SystemManager.system_create(sys)
            SystemManager.subscribe(entity_id, sys)

    @classmethod
    def component_remove(cls, entity_id, comp):
        ent = cls.entity_get(entity_id)
        if comp in ent.components:
            ent.components.pop(comp)


class SystemManager:
    active_systems = set()

    @classmethod
    def system_create(cls, sys):
        if sys not in cls.active_systems:
            cls.active_systems.add(sys)

    @classmethod
    def system_remove(cls, sys):
        if sys in cls.active_systems:
            cls.active_systems.remove(sys)

    @classmethod
    def subscribe(cls, entity_id, sys):
        sys.subscribers.append(EntityManager.entity_get(entity_id))

    @classmethod
    def update(cls):
        for sys in cls.active_systems:
            sys.update()

