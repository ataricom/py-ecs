import ecs_core

entity_manager = ecs_core.EntityManager()
system_manager = ecs_core.SystemManager()
entity_manager.entity_create()
entity_manager.entity_create()

ent0 = entity_manager.entity_pool[0]
ent1 = entity_manager.entity_pool[1]

entity_manager.component_add(0, 'Position')
for ent_id, ent in enumerate(entity_manager.entity_pool):
    print('entity: {} has {} components'.format(ent_id, entity_manager.entity_pool[ent_id].components))

print('active systems', system_manager.active_systems)

ent0_position = ent0.get_component('Position')

print(ent0_position)
system_manager.update()
print(ent0_position)
