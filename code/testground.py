import pygame
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vital Monitor")

GREEN = (0, 180, 0)
WHITE = (255, 255, 255)

font_big = pygame.font.SysFont(None, 120)
font_small = pygame.font.SysFont(None, 60)

clock = pygame.time.Clock()

# Sequence of numbers
sequence = [
    6, 148, 180,
    170, 146,
    155, 171,
    192, 175, 157,
    135, 110, 103, 98, 86, 82
]

# Timing
TOTAL_TIME = 39  # seconds
FPS = 60
total_jumps = len(sequence) - 1
interval_frames = TOTAL_TIME * FPS / total_jumps  # frames between jumps

current_index = 0
frame_counter = 0
running_counter = False
finished = False

running = True
while running:
    clock.tick(FPS)
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not running_counter:
                running_counter = True

    if running_counter and not finished:
        frame_counter += 1
        if frame_counter >= interval_frames:
            frame_counter = 0
            current_index += 1
            if current_index >= len(sequence):
                finished = True
                current_index = len(sequence) - 1  # stay at last number

    # DISPLAY
    if not finished:
        text = font_big.render(str(sequence[current_index]), True, WHITE)
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, rect)
    else:
        bp_text = font_big.render("147/83", True, WHITE)
        bpm_text = font_small.render("BPM: 53", True, WHITE)

        screen.blit(bp_text, bp_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
        screen.blit(bpm_text, bpm_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60)))

    pygame.display.flip()

pygame.quit()
sys.exit()