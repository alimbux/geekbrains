class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return f'Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return f'Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(f"{pen.title}:")
print(pen.draw())
print(f"{pencil.title}:")
print(pencil.draw())
print(f"{handle.title}:")
print(handle.draw())