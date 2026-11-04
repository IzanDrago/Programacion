import curses
import random
import time
from dataclasses import dataclass


WIN_SCORE = 1000
POINTS_PER_SECOND = 10
PLAYER_X = 8
JUMP_SECONDS = 0.8
OBSTACLE_SPEED = 10


@dataclass
class Obstacle:
    x: float
    symbol: str


def draw_text(screen, y, x, text, width):
    if 0 <= y < screen.getmaxyx()[0] and x < width:
        screen.addnstr(y, max(0, x), text, max(0, width - max(0, x) - 1))


def play_round(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    height, width = screen.getmaxyx()
    start = time.monotonic()
    previous_frame = start
    jump_until = start
    next_obstacle = start + 2
    obstacles = []

    while True:
        now = time.monotonic()
        elapsed = now - start
        score = min(WIN_SCORE, int(elapsed * POINTS_PER_SECOND))
        if score >= WIN_SCORE:
            return "won"

        key = screen.getch()
        if key in (ord("q"), ord("Q")):
            return "quit"
        if key in (ord("w"), ord("W")):
            jump_until = now + JUMP_SECONDS

        delta = now - previous_frame
        previous_frame = now
        if now >= next_obstacle:
            obstacles.append(Obstacle(float(width - 2), random.choice(("&", "2Y", "v"))))
            next_obstacle = now + random.uniform(1.7, 2.5)

        for obstacle in obstacles:
            obstacle.x -= OBSTACLE_SPEED * delta
        obstacles = [obstacle for obstacle in obstacles if obstacle.x + len(obstacle.symbol) > 0]

        jumping = now < jump_until
        player_x = min(PLAYER_X, max(1, width - 4))
        if not jumping and any(
            obstacle.x <= player_x + 1
            and obstacle.x + len(obstacle.symbol) > player_x
            for obstacle in obstacles
        ):
            return "lost"

        screen.erase()
        if height < 8 or width < 30:
            draw_text(screen, 0, 0, "Amplia la terminal para jugar.", width)
        else:
            draw_text(screen, 0, 0, f"Puntos: {score}/{WIN_SCORE}  (10 por segundo)", width)
            draw_text(screen, 1, 0, "Pulsa W para saltar | Q para salir", width)
            ground_y = height - 3
            draw_text(screen, ground_y + 1, 0, "_" * (width - 1), width)
            player_y = ground_y - 2 if jumping else ground_y
            draw_text(screen, player_y, player_x, "D", width)
            for obstacle in obstacles:
                obstacle_y = ground_y - 1 if obstacle.symbol == "v" else ground_y
                draw_text(screen, obstacle_y, int(obstacle.x), obstacle.symbol, width)

        screen.refresh()
        time.sleep(1 / 30)


def wait_after_loss(screen):
    screen.nodelay(False)
    height, width = screen.getmaxyx()
    screen.erase()
    draw_text(screen, height // 2 - 1, 0, "Has perdido.", width)
    draw_text(screen, height // 2, 0, "Pulsa R para reiniciar o Q para salir.", width)
    screen.refresh()
    while True:
        key = screen.getch()
        if key in (ord("r"), ord("R")):
            return "restart"
        if key in (ord("q"), ord("Q")):
            return "quit"


def main(screen):
    while True:
        result = play_round(screen)
        if result == "won":
            return "won"
        if result == "quit" or wait_after_loss(screen) == "quit":
            return "quit"


if __name__ == "__main__":
    outcome = curses.wrapper(main)
    if outcome == "won":
        print("bien echo, toma este logro")
