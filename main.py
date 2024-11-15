import numpy as np

# Кожен квадрат представлений масивом [зверху, зліва, знизу, справа, діагональ]
squares_matrix = [
    [[68, 31, 68, 38, 148], [70, 38, 82, 23, 70], [21, 23, 43, 61, 176], [36, 61, 77, 69, 74], [33, 69, 69, 59, 152]],
    [[68, 90, 17, 32, 98], [82, 32, 63, 71, 132], [43, 71, 46, 34, 134], [77, 34, 87, 25, 138], [69, 25, 16, 63, 132]],
    [[17, 68, 52, 48, 102], [63, 48, 49, 82, 104], [46, 82, 52, 81, 136], [87, 81, 76, 36, 152], [16, 36, 41, 64, 86]],
    [[52, 25, 77, 89, 122], [49, 89, 53, 66, 116], [52, 66, 19, 53, 168], [76, 53, 30, 66, 74], [41, 66, 72, 58, 82]],
    [[77, 33, 53, 24, 132], [53, 24, 28, 25, 116], [19, 25, 43, 21, 144], [30, 21, 63, 48, 114], [72, 48, 31, 51, 188]]
]

start_row, start_col = 4, 0
cost_matrix = np.zeros((len(squares_matrix), len(squares_matrix[0])))
path = [(start_row, start_col)]
selected_edges = []
directions = []

# Функція для відмалювання всього графа
def print_graph(matrix):
    print("\nГраф:")
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            square = matrix[row][col]
            top, left, bottom, right, diagonal = square

            print(f"    ---{top:3}--- ", end="\t")
        print()
        for col in range(len(matrix[row])):
            print(f"   |       /  |", end="\t")
        print()
        for col in range(len(matrix[row])):
            square = matrix[row][col]
            top, left, bottom, right, diagonal = square

            print(f"{left:3}   {diagonal:^5}  {right:3}", end="")
        print()
        for col in range(len(matrix[row])):
            print(f"   |   /      |", end="\t")
        print()
        for col in range(len(matrix[row])):
            square = matrix[row][col]
            top, left, bottom, right, diagonal = square

            print(f"    ---{bottom:3}---", end="\t")
        print("\n")

# Функція для відмалювання одного квадрата
def print_square(row, col, square, direction):
    top, left, bottom, right, diagonal = square

    # Відмалювання квадрата з ребрами та діагоналлю
    print(f"\nКвадрат ({row}, {col}):")
    print(f"    ---{top:3}--- ")
    print(f"   |       /  |")
    print(f"{left:3}   {diagonal:^5}  {right:3}")
    print(f"   |   /      |")
    print(f"    ---{bottom:3}---")
    print(f"Напрямок: {direction}")
    print("")

print_graph(squares_matrix)

# Основний цикл
row, col = start_row, start_col
while row >= 0 and col < len(squares_matrix[0]):
    square = squares_matrix[row][col]
    top, left, bottom, right, diagonal = square

    # Обчислення можливих вартостей шляхів
    path1 = top + left
    path2 = bottom + right
    path3 = diagonal
    min_cost = min(path1, path2, path3)

    # Додаємо напрямок руху, пояснення для обраного шляху, та зберігаємо обрані значення ребер
    if min_cost == path1:
        directions.append("П,С")
        explanation = f"{left} + {top} = {min_cost}"
        selected_edges.append(left)
        selected_edges.append(top)
        print(f"Для квадрата ({row}, {col}) вибираємо шлях з вартістю {min_cost} — П,С ({explanation})")
        print_square(row, col, square, "П,С")
    elif min_cost == path2:
        directions.append("С,П")
        explanation = f"{bottom} + {right} = {min_cost}"
        selected_edges.append(bottom)
        selected_edges.append(right)
        print(f"Для квадрата ({row}, {col}) вибираємо шлях з вартістю {min_cost} — С,П ({explanation})")
        print_square(row, col, square, "С,П")
    elif min_cost == path3:
        directions.append("ПС")
        explanation = f"Діагональ = {min_cost}"
        selected_edges.append(diagonal)
        print(f"Для квадрата ({row}, {col}) вибираємо шлях з вартістю {min_cost} — ПС ({explanation})")
        print_square(row, col, square, "ПС")

    # Зберігаємо вартість у відповідній позиції
    if row == start_row and col == start_col:
        cost_matrix[row, col] = min_cost
    else:
        previous_row, previous_col = row + 1, col - 1
        if previous_row < len(cost_matrix) and previous_col >= 0:
            cost_matrix[row, col] = cost_matrix[previous_row, previous_col] + min_cost
        else:
            cost_matrix[row, col] = min_cost

    print(f"Проміжна вартість: {cost_matrix[row, col]}\n")

    # Зсув на наступну позицію
    row -= 1
    col += 1
    path.append((row, col))

# Відображаємо результати
end_row, end_col = path[-2]
total_min_cost = cost_matrix[end_row, end_col]
print("Результат:")
print(f"Мінімальна вартість шляху:\n\t{total_min_cost}")
print("Шлях:")
print("\t" +" -> ".join(map(str, selected_edges)))
print("Напрями шляху:")
print("\t" + " -> ".join(directions))
print("де П – північ; С – схід; ПС – північний схід.")
