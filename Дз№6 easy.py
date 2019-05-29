import lib_easy as easy_lib

triangle_1 = easy_lib.Triangle('Треугольник_1', [[0,0],
                                                 [2,8],
                                                 [6,4]])

print('Имя фигуры: ', triangle_1.name)
print('Длины сторон: ', triangle_1.get_sides_length())
print('Периметр: ', triangle_1.get_perimeter())
print('Площадь: ', triangle_1.get_square())
print('Высоты: ', triangle_1.get_height())

trapeze_1 = easy_lib.Trapeze('Трапеция_1', [[0,0],
                                            [0,8],
                                            [4,7],
                                            [4,1]])

print('Имя фигуры: ', trapeze_1.name)
print('Длины сторон: ', trapeze_1.get_sides_length())
print('Периметр: ', trapeze_1.get_perimeter())
print('Площадь: ', trapeze_1.get_square())
print('Трапеция равнобочная: ', trapeze_1.trapeze_eq_sides_check())

