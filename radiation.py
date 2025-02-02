import random


class Radiation:
    def __init__(self, game, image):
        self.game = game
        self.image = image
        self.effect = self.image.copy()
        self.effect.set_alpha(0)

    def draw(self, screen, health):
        if health <= 50:
            alpha = 256
            i = random.randint(-10, 10)
            self.effect.set_alpha(alpha - health * 5 + i)
            screen.blit(self.effect, (0, 0))


