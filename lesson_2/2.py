# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = 5
p = 6
print((s**2 - 4)**0.5)
y1 = int((s - (s**2 - 4*p)**0.5)/2)
y2 = int((s + (s**2 - 4*p)**0.5)/2)
x1 = int(p / y1)
x2 = int(p / y2)

print(f'x1:{x1} y1:{y1} x2:{x2} y2:{y2}')

if y1 * x1 == p and y1 + x1 == s:
    print(f"result = {x1} {y1}")
else:
    print(f"result ={x2} {y2}")
