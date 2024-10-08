import threading
import time

class Knight(threading.Thread):
    total_enemies = 100
    lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power =power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while True:
            with self.lock:
                if self.total_enemies <= 0:
                    break
                self.days += 1
                self.total_enemies -= self.power
                remaining_enemies = max(self.total_enemies, 0)
                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")
                time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")