import random

import pygame
import sys
import os

pygame.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космическая игра")

bg_image = pygame.image.load(os.path.join("menubackground.jpg"))
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

BUTTON_COLOR = (70, 70, 80)
HOVER_COLOR = (100, 100, 120)
TEXT_COLOR = (220, 220, 220)
font = pygame.font.Font(None, 42)


class MenuButton:
    def __init__(self, y, text):
        self.width = 280
        self.height = 60
        self.x = WIDTH // 2 - self.width // 2
        self.y = y
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.flag = False

    def draw(self):
        if self.flag:
            color = HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(window, color, self.rect, border_radius=15)

        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        window.blit(text_surf, text_rect)

    def check_flag(self, mouse_pos):
        self.flag = self.rect.collidepoint(mouse_pos)
        return self.flag


class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, m, vx, vy, radius, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.m = m
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.image = pygame.draw.circle(window, pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (self.x, self.y), self.radius)
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)


def main():
    clock = pygame.time.Clock()

    buttons = [
        MenuButton(150, "Новая игра"),
        MenuButton(230, "Загрузить мир"),
        MenuButton(310, "Редактор галактик"),
        MenuButton(390, "Настройки"),
        MenuButton(470, "Выход")
    ]

    """running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.flag:
                        if i == 0:
                            print("Запуск новой игры...")
                        elif i == 1:
                            print("Загрузка сохранения...")
                        elif i == 2:
                            print("Открытие редактора...")
                        elif i == 3:
                            print("Открытие настроек...")
                        elif i == 4:
                            running = False

        window.blit(bg_image, (0, 0))

        for button in buttons:
            button.check_flag(mouse_pos)
            button.draw()

        pygame.display.flip()
        clock.tick(60)"""

    all_sprites = pygame.sprite.Group()

    for i in range(5):
        Planet(random.randint(0, WIDTH), random.randint(0, HEIGHT), 0, 0, 0, 100, all_sprites)

    FPS = 30
    game_run = True
    while game_run:
        clock.tick(FPS)
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
        window.fill(pygame.Color("black"))
        all_sprites.draw(window)
        pygame.display.flip()


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
