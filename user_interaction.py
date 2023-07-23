def show(to_show):
    if to_show == "" or to_show is None:
        print("<Нет данных>")
    else:
        print(to_show)


def read(msg):
    while True:
        input_line = input(msg + "\n")
        if input_line == "" or input_line is None:
            show("Ошибка ввода данных")
        else:
            return input_line

