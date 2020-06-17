import ecs_core
import time


class EntityController(ecs_core.EntityManager):
    pass


class SystemController(ecs_core.SystemManager):
    pass


class Clock:
    start_time = 0
    tick = 1 / 5

    @classmethod
    def cycle_start(cls):
        cls.start_time = time.time()

    @classmethod
    def cycle_end(cls):
        while time.time() < cls.start_time + cls.tick:
            pass
