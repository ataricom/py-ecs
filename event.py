from engine import *


def entity_create():
    EntityController.entity_create()


def entity_remove(entity_id):
    EntityController.entity_remove(entity_id)


def component_add(entity_id, component):
    EntityController.component_add(entity_id, component)


def component_remove(entity_id, component):
    EntityController.component_remove(entity_id, component)


def update():
    SystemController.update()


def dump(entity_id):
    ent = EntityController.entity_get(entity_id)
    print(f'entity {entity_id}')
    for comp in ent.components:
        print(ent.components[comp])
    print()


def dump_all():
    for ent in EntityController.entity_pool:
        dump(ent)
