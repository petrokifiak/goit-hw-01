import turtle

def koch_curve(pen, length, level):
    if level == 0:
        pen.forward(length)
    else:
        length /= 3.0
        koch_curve(pen, length, level - 1)
        pen.left(60)
        koch_curve(pen, length, level - 1)
        pen.right(120)
        koch_curve(pen, length, level - 1)
        pen.left(60)
        koch_curve(pen, length, level - 1)

def draw_koch_snowflake(pen, length, level):
    for _ in range(3):
        koch_curve(pen, length, level)
        pen.right(120)

def main():
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха (наприклад, 3): "))
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title(f"Сніжинка Коха - Рівень {level}")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()

    draw_koch_snowflake(pen, 400, level)
    turtle.done()

if __name__ == "__main__":
    main()
