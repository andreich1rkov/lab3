def is_same_color(k, l, m, n):
    if (k + l) % 2 == (m + n) % 2:
        return True
    else:
        return False

def is_threatened(k, l, m, n, figure):
    if figure == "ферзь" or figure == "ладья":
        if k == m or l == n:
            return True
    if figure == "ферзь" or figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
    if figure == "конь":
        if abs(k - m) == 2 and abs(l - n) == 1:
            return True
        if abs(k - m) == 1 and abs(l - n) == 2:
            return True
    return False

def can_reach(k, l, m, n, figure):
    if figure == "ладья":
        if k == m or l == n:
            return True
    if figure == "ферзь":
        if k == m or l == n or abs(k - m) == abs(l - n):
            return True
    if figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
    return False


k = int(input("Введите номер вертикали поля K (1-8): "))
l = int(input("Введите номер горизонтали поля K (1-8): "))
m = int(input("Введите номер вертикали поля M (1-8): "))
n = int(input("Введите номер горизонтали поля M (1-8): "))
print()

figure = input("Введите фигуру на поле K (ферзь, ладья, слон, конь): ")
print()

print("а) Поля (k, l) и (m, n) являются полями одного цвета:", is_same_color(k, l, m, n))
print("б) Фигура угрожает полю (m, n):", is_threatened(k, l, m, n, figure))
print("в) Фигура может попасть на поле (m, n) одним ходом:", can_reach(k, l, m, n, figure))