import time as t


class Timer:
    def __init__(self, **kwargs):
        # Вход
        self.input = kwargs['input']
        # Выход
        self.output = None
        # Время
        self.time = kwargs['time']
        # Счетчик, мс
        self.counter = 0
        # Задание таймера в секундах или Мс
        self.timer_limit = self.time.split('#')

    def set(self):
        self.time = int(self.timer_limit[0])
        if self.input:
            while self.counter < self.time:
               if 'MS' in self.timer_limit:
                    self.counter += 1
                    t.sleep(0.001)
                    self.print_timer_status()
               else:
                   self.counter += 1
                   self.print_timer_status()
                   t.sleep(1)

            self.output = True

    def reset(self):
        self.output = False
        self.counter = 0
        if self.input:
            self.set()

    def print_timer_status(self):
        if 'MS' in self.timer_limit:
            print(f'{self.counter} ms / {self.time} ms')
        else:
            print(f'{self.counter} s / {self.time} s')


