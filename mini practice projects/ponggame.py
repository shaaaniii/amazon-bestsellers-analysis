import pygame
import random
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

def main():
    # GAME SETUP
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Game")

    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    paddle_1_move = 0
    paddle_2_move = 0

    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    # create the clock object to keep track of the time
    clock = pygame.time.Clock()

    """
    this is to check whether or not to move the ball
    we will make it move after 3 seconds
    """
    started = False

    # game loop
    while True:
        screen.fill(COLOR_BLACK)

        # make the ball move after 3 seconds
        if not started:
            # load the Consolas font
            font = pygame.font.SysFont('Consolas', 30)

            # draw some text to the center of the screen
            text = font.render('Press Space to Start', True, COLOR_WHITE)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)

            # update the display
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
            continue  # prevents running rest of loop before starting

        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # if the user is pressing a key
            if event.type == pygame.KEYDOWN:

                # PLAYER 1
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5

                # PLAYER 2
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5

            # if the player released a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_move = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move = 0.0

        # get delta time
        delta_time = clock.tick(60)

        # move paddles
        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time

        # draw paddles
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

        # draw ball
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        pygame.display.update()

        # if the ball goes out of bounds, end the game
        if ball_rect.left <= 0 or ball_rect.left >= SCREEN_WIDTH:
            return

        # ball collision with top
        if ball_rect.top < 0:
            ball_accel_y *= -1
            ball_rect.top = 0

        # ball collision with bottom
        if ball_rect.bottom > SCREEN_HEIGHT - ball_rect.height:
            ball_accel_y *= -1
            ball_rect.top = SCREEN_HEIGHT - ball_rect.height

        # paddle collisions
        if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left += 5

        if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left -= 5

        # move ball
        if started:
            ball_rect.left += ball_accel_x * delta_time
            ball_rect.top += ball_accel_y * delta_time


if __name__ == "__main__":
    main()
