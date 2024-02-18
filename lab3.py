
import os.path
import csv


def print_dict(d):
    print('')
    for k, v in d.items():
        print(str(k) + '\t' + str(v['workplace_flag']) + '\t' + str(v['room_number'])
              + '\t' + v['date_time'] + '\t' + str(v['movement_id']))


def sort_by_string_field(data, field):
    return dict(sorted(data.items(), key=lambda f: f[1][field]))


def sort_by_numeric_field(data, field):
    return dict(sorted(data.items(), key=lambda f: int(f[1][field])))


def filter_by_criteria(data, field, value):
    return dict((k, v) for k, v in data.items() if v[field] > value)


def add_movement_to_dict(file, data, movement_id, date_time, workplace_flag, room_number):
    writer = csv.writer(file, delimiter=';')

    # записываем текущие данные в файл
    for k, v in data.items():
        writer.writerow([k, v['date_time'], v['workplace_flag'], v['room_number']])

    # добавляем новое перемещение в словарь
    data[len(data) + 1] = {'date_time': date_time,
                           'workplace_flag': workplace_flag,
                           'room_number': room_number,
                           'movement_id': movement_id}

    # записываем новые данные в файл
    writer.writerow([len(data), date_time, workplace_flag, room_number, movement_id])


directory_path = "C:/Users/Eugene/PycharmProjects/lab3"  # Путь к директории, которую нужно обработать

# Подсчет количества файлов в директории
num_files = len([file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))])
print(f"Количество файлов в директории {directory_path}: {num_files}")

csv_filename = "MyCsv.csv"  # Имя файла с данными

# Считывание данных из CSV-файла
data = {}
with open(csv_filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if len(row) < 5:
            continue
        data[int(row[0])] = {
            'date_time': row[1],
            'workplace_flag': bool(row[2]),
            'room_number': int(row[3]),
            'movement_id': int(row[4])
        }

# Вывод информации о перемещениях
print_dict(data)

# Вывод информации об объектах, отсортированных по строковому полю `date_time`
sorted_by_string = sort_by_string_field(data, "date_time")
print("Данные, отсортированные по дате и времени:")
print_dict(sorted_by_string)

# Вывод информации об объектах, отсортированных по числовому полю `movement_id`
sorted_by_numeric = sort_by_numeric_field(data, "movement_id")
print("Данные, отсортированные по номеру перемещения:")
print_dict(sorted_by_numeric)

# Вывод информации, соответствующей критерию - перемещениям в определенную комнату
filtered_data = filter_by_criteria(data, "room_number", 5)
print("Данные, соответствующие перемещениям в комнату 5:")
print_dict(filtered_data)

# Добавление новых данных и запись их в CSV-файл
with open(csv_filename, 'a', newline='') as csvfile:
    add_movement_to_dict(csvfile, data, 40, "2023-05-01 14:00:00", False, 3)
    add_movement_to_dict(csvfile, data, 41, "2023-05-31 12:00:00", True, 2)