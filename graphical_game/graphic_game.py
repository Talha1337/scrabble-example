import pygame

pygame.font.init()
TILEWIDTH = 600 / 15


# TODO: Track presence of different tiles


def coord_to_px(coords: tuple[int, int]) -> tuple[int, int]:
    return tuple([int((TILEWIDTH) * coord) for coord in coords])


class ScrabbleGraphicGame:
    def __init__(self):
        pygame.init()
        self.surf = pygame.display.set_mode((600, 800))
        self.bg_image = pygame.image.load("images/scrabble_board_img.jpg")
        self.available_letters = [
            pygame.Rect(50 + i * 75, 650, 40, 40) for i in range(7)
        ]
        self.active_tile = None

    def populate_with_coords(self):
        for i in range(15):
            for j in range(15):
                coord_value = (i, j)
                px_value = coord_to_px(coord_value)
                pygame.draw.circle(self.surf, (255, 0, 0), px_value, 10)

    def add_bg(self):
        self.surf.fill("green")
        self.surf.blit(self.bg_image, (0, 0))

    def add_tile_to_board(self, pos: tuple[int, int]):
        """
        Adding the white scrabble tile to the point.
        """
        pygame.draw.rect(self.surf, (255, 255, 255), (pos[0], pos[1], 40, 40))

    def add_letter_to_board(self, pos: tuple[int, int], letter: str):

        my_font = pygame.font.SysFont("Calibri", 36, bold=True)
        text_surface = my_font.render(letter, False, (0, 0, 0))
        letter_pos = (pos[0] + TILEWIDTH / 5, pos[1])
        self.surf.blit(text_surface, letter_pos)

    def add_scrabble_tile(self, pos: tuple[int, int], letter: str):
        self.add_tile(pos)
        self.add_letter(pos, letter)

    def get_letters_at_bottom(self, letters: str | list):
        for i, letter in enumerate(self.available_letters):
            letter_rect = pygame.Rect(50 + i * 75, 650, 40, 40)
            pygame.draw.rect(self.surf, (255, 255, 255), letter_rect)


# Setting game window dimensions
game_display = ScrabbleGraphicGame()
# bg_image = pygame.transform.scale(bg_image, (1, 1))
# Main game loop
running = True

while running:
    game_display.add_bg()
    game_display.populate_with_coords()
    game_display.add_tile_to_board(coord_to_px((0, 0)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
            if event.button == 1:
                for i, letter in enumerate(game_display.available_letters):
                    if letter.collidepoint(event.pos):
                        game_display.active_tile = i
        if event.type == pygame.MOUSEBUTTONUP:
            print("unclick")
            game_display.active_tile = None
        if event.type == pygame.MOUSEMOTION:
            if game_display.active_tile is not None:
                print(event.rel)
                game_display.available_letters[i].move_ip(event.rel)

    # Drawing image at position (0,0)
    pygame.display.flip()
pygame.quit()
