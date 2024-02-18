import os

p = 'C:/Users/marga/PycharmProjects/pythonProject14'
print('Файлов в папке ' + p + ': ' + str(len(os.listdir(p))))


class Row:
    idx = 0

    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val


class OfficeMove(Row):
    idx, date, is_workplace, room_num = 0, '', False, 0

    def __init__(self, idx: int, date: str, is_workplace: bool, room_num: int):
        super().__init__(idx)
        self.idx = idx
        self.date = date
        self.is_workplace = is_workplace
        self.room_num = room_num

    def __str__(self):
        return f'№{self.idx}, дата и время: {self.date}, рабочее место: {self.is_workplace}, номер комнаты: {self.room_num}'

    def __repr__(self):
        return f'OfficeMove(idx={self.idx},date="{self.date}",is_workplace={self.is_workplace},room_num={self.room_num})'

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Data:
    file_path = ''
    data = {}
    pointer = 0

    def __init__(self, file):
        self.file_path = file
        self.data = self.parse(file)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f'Контейнер хранит в себе следущее:\n{d_str}'

    def __repr__(self):
        return f'Data({[repr(rm) for rm in self.data]})'

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            self.pointer += 1
            return self.data[self.pointer - 1]

    def __getitem__(self, ite):
        if not isinstance(ite, int):
            raise TypeError('Индекс должен быть целым числом')
        if 0 <= ite < len(self.data):
            return self.data[ite]
        else:
            raise IndexError('Неверный индекс')

    def as_generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    @staticmethod
    def parse(file):
        parsed = []
        with open(file, "r") as raw_csv:
            for line in raw_csv:
                (idx, date, is_workplace, room_num) = line.replace("\n", "").split(";")
                parsed.append(
                    OfficeMove(int(idx), date, bool(is_workplace), int(room_num))
                )
        return parsed

    def sorted_by_date(self):
        return sorted(self.data, key=lambda f: f.date)

    def sorted_by_room_num(self):
        return sorted(self.data, key=lambda f: f.room_num)

    def value(self, value):
        r = []
        for d in self.data:
            if d.room_num == value:
                r.append(d)
        return r

    def add_new(self, date, is_workplace, room_num):
        self.data.append(
            OfficeMove(len(self.data) + 1, date, is_workplace, room_num)
        )
        self.save(self.file_path, self.data)

    @staticmethod
    def save(file, new_data):
        with open(file, "w", encoding='utf-8') as f:
            for r in new_data:
                f.write(f"{r.idx};{r.date};{int(r.is_workplace)};{r.room_num}\n")

    def print(self):
        for r in self.data:
            print(f'№{r.idx}, дата и время: {r.date}, рабочее место: {r.is_workplace}, номер комнаты: {r.room_num}')

    @staticmethod
    def print_d(d):
        for r in d:
            print(f'№{r.idx}, дата и время: {r.date}, рабочее место: {r.is_workplace}, номер комнаты: {r.room_num}')


data = Data("data.csv")

# __repr__()
print(repr(data), "\n")

print('str вывод')
# __str__()
print(data, "\n")

print('итератор вывод')
# Итератор
for item in iter(data):
    print(item)
print('')

# Генератор
for item in data.as_generator():
    print(item)
print('')
print('сортировка по дате')
data.print_d(data.sorted_by_date())  # сортировка по дате
print('')
print('сортировка по номеру комнаты')
data.print_d(data.sorted_by_room_num())  # сортировка по номеру комнаты
print('')
print('номер  103')
data.print_d(data.value(103))  # номер комнаты равен 103
