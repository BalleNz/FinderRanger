def clr(area):
    a = "\n" * area
    print(a, a)  # x2


def find_divs(i):
    a = [
        [d] if d ** 2 == i
        else [d, i // d]
        for d in range(1, int(i ** 0.5) + 1)
        if i % d == 0
    ]
    new_a = []
    for j in a:
        new_a += j
    return sorted(new_a)


def find_simple_d(i: int):
    a = find_divs(i)
    j = (j for j in a if len(find_divs(j)) == 2)
    while True:
        try:
            print(f" {next(j)}", end=" ")
        except:
            break
    print("\n")


def main_help():
    print(
        " 1. Finder\n"
        " 2. RangeR\n\n\n"
        "\u2192", end=" "
    )


def main():
    main_help()
    choice = 1
    while not 1 > choice > 2:
        try:
            choice = int(input())
            if choice > 2 or choice < 0:
                clr(40)
                print("please oT odnogo do second")
                clr(10)
                main_help()
                continue
            else:
                break
        except:
            clr(40)
            print("please integer")
            clr(10)
            main_help()
    return choice


def answ(choice: int):
    clr(40)
    if choice == 1:
        i = int(input(
            "Какое число?\n\n\n"
            "\u2192  "
        ))
        clr(40)
        return i
    elif choice == 2:
        clr(42)
        a = int(input(
            "\n С какого диапазона? #включительно\n\n\n\u2192"
        ))
        clr(4)
        b = int(input(
            " До какого диапазона? #включительнo\n\n\n\u2192"
        ))
        clr(4)
        return [a, b]


def ranger_main(answ: int):
    if answ == 1:
        clr(4)
        return int(input(
            "Нумерация: \n"
            "  1. Обычная\n"
            "  2. Сложная\n\n\n\u2192"
        ))
    elif answ == 2:
        clr(4)
        return int(input(
            "Сколько делителей?\n"
            " \n\n\n\u2192"
        ))
    elif answ == 3:
        clr(4)
        return int(input(
            "На какое число ?\n\n\n\n"
            "\u2192"
        ))
    elif answ == 4:
        clr(4)
        return int(input(
            "Нумерация:\n"
            "  1. Обычная\n"
            "  2. Сложная\n\n\n\u2192"
        ))
def ranger_find_for_division(division, a, b):
    lenght, count, count_temp = 0, 0, 0
    for i in range(a, b+1):
        count_temp += 1
        a = find_divs(i)
        if division in a:
            lenght += 1
            print(f"Number: {i} | Length of Divs: {len(find_divs(i))} | Порядковый номер: {count_temp}")
    print(f"________________________________________________________\nКоличество чисел делящихся на {division}:  {lenght}\n")
def ranger_find_simple(numeration, a, b):
    lenght, count, count_temp = 0, 0, 0
    for i in range(a, b+1):
        count_temp += 1
        if len(find_divs(i)) == 2:
            lenght += 1
            if numeration == 1:
                count = lenght
            else: count = count_temp
            print(f"All Simples (all divs): {find_divs(i)} | Number: {i} | Порядковый номер: {count}")
    print(f"________________________________________________________\nВсего Простых Чисел:  {lenght}\n")
    return "\n "
def ranger_find_for_counts(need_count, a, b):
    length, count = 0, 0
    for i in range(a, b+1):
        count += 1
        if len(find_divs(i)) == need_count:
            length += 1
            print(f"Number: {i} | Length of Divs: {len(find_divs(i))} | Порядковый номер: {count}")
def ranger_find_sqrt(numeration, a, b):
    count, length, count_temp = 0, 0, 0
    for i in range(a, b+1):
        count_temp += 1
        if int(i**0.5)*int(i**0.5) == i:
            if numeration == 2:
                count = count_temp
            else:
                count = length
            length += 1
            print(f"Number: {i} | Length of Divs: {len(find_divs(i))} | Порядковый номер: {count}")
    print(f"________________________________________________________\nВсего чисел с корнем:  {length}")
def ranger_job(what_to_do, optional, answer):
    a, b = answer[0], answer[1]
    if what_to_do == 1:
        ranger_find_simple(optional, a, b)
    elif what_to_do == 2:
        ranger_find_for_counts(optional, a, b)
    elif what_to_do == 4:
        ranger_find_sqrt(optional, a, b)
    elif what_to_do == 3:
        ranger_find_for_division(optional, a,b)

a = 2002002002
b = 2002002002
i = 2002002002
clr(40)
while True:
    choice = main()
    try:
        answer = answ(choice)
        if type(answer) == list:
            try:
                ranger_answer = int(input(
                    "Что нужно сделать? \n\n"
                    "  1. Найти простые числа\n"
                    "  2. Поиск по кол-ву делителей\n"
                    "  3. Делимость на число N\n"
                    "  4. Проверка на корень\n\n\n\n\n\u2192"
                ))
                if ranger_answer not in [1, 2, 3, 4]:
                    clr(40)
                    print("Нет такого пункта и никогда не было.\n\n\n")
                    continue
                else:
                    ranger_optional = ranger_main(ranger_answer)
                    ranger_job(ranger_answer, ranger_optional, answer)
            except:
                clr(30)
                print("Input Error\n\n\n")
                continue
        elif type(answer) == int:
            print(f"\n Делители числа {answer}: \n {find_divs(answer)}")
            print(" Из них простые: ", end="")
            find_simple_d(answer)
        else:
            clr(30)
            print("Only integer's, Please!")
            continue
    except:
        clr(4)
        print("error какойта")
        clr(5)