from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemies = 100
        days = 0
        print(f'Sir {self.name}, на нас напали!')
        while enemies > 0:
            enemies -= self.skill
            days += 1
            print(f'Sir {self.name} сражается {days} день(дня)..., осталось {enemies if enemies > 0 else 0} воинов.')
            time.sleep(0.4)
        print(f'Sir {self.name} одержал победу спустя {days} дней!')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')