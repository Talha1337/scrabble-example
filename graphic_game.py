import pygame


def coord_to_px(coords: tuple[int, int]) -> tuple[int, int]:
    return tuple([int((600 / 15) * coord) for coord in coords])


def populate_with_coords(surf: pygame.Surface) -> pygame.Surface:
    for i in range(15):
        for j in range(15):
            coord_value = (i, j)
            px_value = coord_to_px(coord_value)
            print(px_value)
            pygame.draw.circle(surf, (255, 0, 0), px_value, 10)
    return surf


def add_letters(surf: pygame.Surface, pos: tuple[int, int]) -> pygame.Surface:
    pass


pygame.init()
# Setting game window dimensions
window_width = 600
window_height = 800  # Want the extra 200 for placing tiles on and stuff
game_display = pygame.display.set_mode((window_width, window_height))
game_display.fill("green")
# Loading the image
bg_image = pygame.image.load("images/scrabble_board_img.jpg")
# bg_image = pygame.transform.scale(bg_image, (1, 1))
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Drawing image at position (0,0)
    game_display.blit(bg_image, (0, 0))
    game_display = populate_with_coords(game_display)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
