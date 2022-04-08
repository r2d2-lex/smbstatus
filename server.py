from flask import Flask, render_template
from smbstat import smb_status
from collections import namedtuple
import re

app = Flask(__name__)
SKIP_LINES = 4


def parse_status(smb_data):
    status_record = []
    Records = namedtuple('RECORDS', 'Pid Uid DenyMode Access R_W Op_lock SharePath Name Time')
    count = 0
    for line in smb_data.splitlines():
        count += 1
        if count < SKIP_LINES:
            continue
        parsed_line = parse_line(line)
        if not parsed_line:
            continue

    return status_record


def parse_line(line):
    split_line = line.split('/', 1)
    try:
        part1 = split_line[0]
        part2 = split_line[1]
    except IndexError:
        return False

    part1_list = parse_part1(part1)
    part2_list = parse_part2(part2)
    if not part2_list:
        return False

    list_of_string = part1_list + part2_list
    print(f'Parsed string: {list_of_string}')
    return list_of_string


def parse_part1(part1):
    return part1.split()


def parse_part2(part2):
    """
        Возвращает список ['шара','путь к файлу','время доступа']
    :param part2:
    :return:
    """
    share_index = 0
    path_date_index = 1
    try:
        string_split = part2.split(' ', 1)
    except ValueError:
        return False

    try:
        name_of_share = string_split[share_index]
        path_date_part = string_split[path_date_index]
    except IndexError:
        return False

    path_time_list = get_file_path_time(path_date_part)
    if not path_time_list:
        return False

    return_part2_list = [name_of_share] + path_time_list
    return return_part2_list


def get_file_path_time(path_time_part):
    """
        Получаем имя файла и дату
        Ищем регуляркой: Пример: длиное_имя_файла.txt  Fri Apr  7 01:12:34 2022
    :param path_time_part:
    :return: Список ['мия файла/папки', 'дата доступа']
    """
    need_tuple_size = 2
    path_time_part = path_time_part.strip()
    re_value = re.findall(r'(.*)\s+(\w{3}\s+\w{3}\s+[0-9]{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2}\s+\d{4})$', path_time_part)
    try:
        re_value_tuple = re_value[0]
    except IndexError:
        return False

    re_value_size = len(re_value_tuple)
    if re_value_size < need_tuple_size:
        return False

    try:
        path_of_file = re_value_tuple[0]
        time_of_access = re_value_tuple[1]
    except IndexError:
        return False

    path_of_file = path_of_file.rstrip()
    return [path_of_file, time_of_access]


@app.route('/')
def index():
    page_title = 'SambaStatus'
    smb_data = smb_status()
    smb_lines = parse_status(smb_data)
    return render_template('index.html', page_title=page_title, smb_lines=smb_lines)


def main():
    smb_data = smb_status()
    smb_lines = parse_status(smb_data)


if __name__ == '__main__':
    main()
    # app.run(debug=True)
