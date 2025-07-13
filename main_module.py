import pygame
from timer import Timer


class Main:
    def __init__(self, **kwargs):
        self.timer_1 = Timer(input=kwargs['input_1'], time=kwargs['time_1'])
        self.timer_2 = Timer(input=kwargs['input_2'], time=kwargs['time_2'])

        pygame.init()
        self.screen = pygame.display.set_mode((300, 670))
        pygame.display.set_caption("Q3")

        self.simulation_started = False

        # Координаты и размеры кнопки
        self.button_rect = pygame.Rect(90, 600, 120, 40)

        self.leds = {
            'Q1': False,
            'Q2': False,
            'Q3': False,
            'Q4': False,
            'Q5': False,
            'Q6': False,
            'Q7': False,
            'Q8': False,
        }
        self.leds_status = {
            'Q1': False,
            'Q2': False,
            'Q3': False,
            'Q4': False,
            'Q5': False,
            'Q6': False,
            'Q7': False,
            'Q8': False,
        }

    def draw_start_button(self):
        pygame.draw.rect(self.screen, (70, 130, 180), self.button_rect, border_radius=8)
        font = pygame.font.SysFont(None, 28)
        text = font.render("Start", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.button_rect.center)
        self.screen.blit(text, text_rect)

    def draw_leds(self, screen, leds):
        self.screen.fill((20, 20, 20))  # Тёмный фон

        width = 60
        height = 60
        spacing = 20
        start_x = 100
        start_y = 30

        colors = {
            True: (0, 255, 0),  # Включён — зелёный
            False: (60, 60, 60)  # Выключен — серый
        }

        font = pygame.font.SysFont(None, 20)

        # Преобразуем список светодиодов в список и идём по вертикали
        for i, (led, value) in enumerate(leds.items()):
            x = start_x
            y = start_y + i * (height + spacing)
            pygame.draw.rect(screen, colors[value], (x, y, width, height), border_radius=10)

            label = font.render(led, True, (255, 255, 255))
            screen.blit(label, (x + width + 10, y + height // 2 - 10))

        pygame.display.flip()

    def generate(self):
        self.timer_1.input = True
        self.timer_1.set()

        while True:
            if self.timer_1.output:
                if not self.leds_status['Q1']:
                    self.leds['Q1'] = True

                if self.leds_status['Q1'] and not self.leds_status['Q2']:
                    self.leds['Q1'] = False
                    self.leds['Q2'] = True

                if self.leds_status['Q1'] and self.leds_status['Q2'] and not self.leds_status['Q3']:
                    self.leds['Q2'] = False
                    self.leds['Q3'] = True

                if (self.leds_status['Q1'] and self.leds_status['Q2'] and self.leds_status['Q3']
                        and not self.leds_status['Q4']):
                    self.leds['Q3'] = False
                    self.leds['Q4'] = True

                if (self.leds_status['Q1'] and self.leds_status['Q2']
                        and self.leds_status['Q3'] and self.leds_status['Q4']
                        and not self.leds_status['Q5']):
                    self.leds['Q4'] = False
                    self.leds['Q5'] = True

                if (self.leds_status['Q1'] and self.leds_status['Q2']
                        and self.leds_status['Q3'] and self.leds_status['Q4']
                        and self.leds_status['Q5'] and not self.leds_status['Q6']):
                    self.leds['Q5'] = False
                    self.leds['Q6'] = True

                if (self.leds_status['Q1'] and self.leds_status['Q2'] and self.leds_status['Q3']
                        and self.leds_status['Q4'] and self.leds_status['Q5']
                        and self.leds_status['Q6'] and not self.leds_status['Q7']):
                    self.leds['Q6'] = False
                    self.leds['Q7'] = True

                if (self.leds_status['Q1'] and self.leds_status['Q2'] and self.leds_status['Q3']
                        and self.leds_status['Q4'] and self.leds_status['Q5']
                        and self.leds_status['Q6'] and self.leds_status['Q7']
                        and not self.leds_status['Q8']):
                    self.leds['Q7'] = False
                    self.leds['Q8'] = True

                if self.leds['Q1']:
                    self.leds_status['Q1'] = True

                if self.leds['Q2']:
                    self.leds_status['Q2'] = True

                if self.leds['Q3']:
                    self.leds_status['Q3'] = True

                if self.leds['Q4']:
                    self.leds_status['Q4'] = True

                if self.leds['Q5']:
                    self.leds_status['Q5'] = True

                if self.leds['Q6']:
                    self.leds_status['Q6'] = True

                if self.leds['Q7']:
                    self.leds_status['Q7'] = True

                self.draw_leds(self.screen, self.leds)
                self.timer_2.input = True
                self.timer_2.set()

                if self.leds['Q8']:
                    for key in self.leds.keys():
                        self.leds[key] = False
                    for key in self.leds_status.keys():
                        self.leds_status[key] = False

            if self.timer_2.output:
                self.timer_1.reset()
                self.timer_2.input = False
                self.timer_2.reset()
