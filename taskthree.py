print("Длина маршрута велоралли 100 километров за 10 часов по Поясу Славы - примерно 100 километров.")
print("Велосипедист Вася стартует с нулевого километра маршрута и едет со скоростью `v` километров в час.")
print("На какой отметке он остановится через `t` часов?")
print("Введите скорость Васи в км.ч")
v = int(input())
if v > 0:
        print("Введите время поездки в часах")
        t = int(input())
        s = v * t
        sint = int(s)
        sstr = str(sint)
        print("Вася проехал " + sstr + " киллометра(ов)")
        if s > 100:
            division = s - 100
            divisionstr = str(division)
            print("Вамя проехал финиш " + divisionstr + " киллометров назад")
else:
    if v < 0:
        print("Вася сбежал")
