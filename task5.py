def square(side):
    square_quadrate = side ** 2
    perimeter = side * 4
    diagonal = square_quadrate / 2
    result = (square_quadrate, perimeter, diagonal)
    return result

print(square(5))