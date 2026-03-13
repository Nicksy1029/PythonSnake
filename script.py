import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
DIRECTIONS = ['Up', 'Down', 'Left', 'Right']
CELL_SIZE = 10
DELAY = 100

root = tk.Tk()
root.title('Змейка | Счет: 0')
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width = WIDTH,
    height = HEIGHT,
    bg = 'black',
    highlightthickness = 0
)
canvas.pack()

snake = [(100, 100), (90, 100), (80, 100)]
direction = 'Right'
score = 0
game_over = False

def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

def draw_food():
    canvas.create_rectangle(
        food[0], food[1],
        food[0] + CELL_SIZE,
        food[1] + CELL_SIZE,
        fill = 'red'
    )

def draw_snake():
    for segment in snake:
        canvas.create_rectangle(
            segment[0], segment[1],
            segment[0] + CELL_SIZE,
            segment[1] + CELL_SIZE,
            fill = 'green',
            outline = 'darkgreen'
        )

def on_key_press(event):
    global direction
    key = event.keysym
    if key in DIRECTIONS:
        if (key == 'Up' and direction != 'Down' or key == 'Down' and direction != 'Up' or
        key == 'Left' and direction != 'Right' or key == 'Right' and direction != 'Left'):
            direction = key

root.bind("<KeyPress>", on_key_press)

def move_snake():
    head_x, head_y = snake[0]

    if direction == 'Up':
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == 'Down':
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == 'Left':
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == 'Right':
        new_head = (head_x + CELL_SIZE, head_y)

    snake.insert(0, new_head)
    if not check_food_collision():
        snake.pop()

def check_food_collision():
    global food, score
    if snake[0] == food:
        score+=1
        food = create_food()
        return True
    return False

def update_title():
    root.title(f"Змейка | Счет: {score}")

def check_wall_collision():
    head_x, head_y = snake[0]
    return (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT
    )

def end_game():
    global game_over
    game_over = True
    canvas.create_text(
        WIDTH // 2, HEIGHT // 2,
        text=f"Game Over! Score: {score}",
        fill = 'white',
        font=('Arial', 24)
    )

def game_loop():
    global snake, food, score

    if game_over:
        return

    move_snake()

    if check_wall_collision():
        end_game()
        return

    canvas.delete('all')
    draw_food()
    draw_snake()
    update_title()
    root.after(DELAY, game_loop)


food = create_food()
draw_food()
draw_snake()
root.after(DELAY, game_loop)

root.mainloop()
