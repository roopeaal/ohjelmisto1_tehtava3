import random


def calculate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    estimated_pi = 4 * points_inside_circle / num_points
    return estimated_pi


# Kysytään käyttäjältä arvottavien pisteiden määrä
num_points = int(input("Syötä arvottavien pisteiden määrä: "))

estimated_pi = calculate_pi(num_points)
print(f"Laskettu piin likiarvo {num_points} arvotulla pisteellä: {estimated_pi}")
