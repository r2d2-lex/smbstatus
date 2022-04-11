from getuserlist import make_uid_users_dict, check_uid

from flask import Flask, render_template
from smbstat import smb_status
from collections import namedtuple
import re

app = Flask(__name__)
SKIP_LINES = 4
UID = 1
# Pid          Uid        DenyMode   Access      R/W        Oplock
SIZE_LIST_OF_PART1 = 6
# SharePath   Name   Time
SIZE_LIST_OF_PART2 = 3
PATH_TIME_LIST_SIZE = 2


def parse_status(smb_data, uid_users_dict):
    """
    # 'Pid Uid DenyMode Access R_W Op_lock SharePath Name Time LoginName'
    :param smb_data:
    :param uid_users_dict:
    :return:
    """
    status_records = []
    count = 0
    for line in smb_data.splitlines():
        count += 1
        if count < SKIP_LINES:
            continue
        parsed_line = parse_line(line)
        if not parsed_line:
            continue

        try:
            username = check_uid(parsed_line[UID], uid_users_dict)
        except IndexError:
            continue

        parsed_line.append(username)
        print(f'Parsed string: {parsed_line}')
        status_records.append(parsed_line)

    return status_records


def parse_line(line) -> list:
    """
        Создаём список из параметров
    :param line:
    :return:
    """
    split_line = line.split('/', 1)
    try:
        part1 = split_line[0]
        part2 = split_line[1]
    except IndexError:
        return []

    part1_list = parse_part1(part1)
    if len(part1_list) < SIZE_LIST_OF_PART1:
        print('Part1 bad size')
        return []

    part2_list = parse_part2(part2)
    if len(part2_list) < SIZE_LIST_OF_PART2:
        print('Part2 bad size')
        return []

    list_of_string = part1_list + part2_list
    return list_of_string


def parse_part1(part1) -> list:
    return part1.split()


def parse_part2(part2) -> list:
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
        return []

    try:
        name_of_share = string_split[share_index]
        path_date_part = string_split[path_date_index]
    except IndexError:
        return []

    path_time_list = get_file_path_time(path_date_part)
    if len(path_time_list) < PATH_TIME_LIST_SIZE:
        return []

    return_part2_list = [name_of_share] + path_time_list
    return return_part2_list


def get_file_path_time(path_time_part) -> list:
    """
        Получаем имя файла и дату
        Ищем регуляркой: Пример: длиное_имя_файла.txt  Fri Apr  7 01:12:34 2022
    :param path_time_part:
    :return: Список ['имя файла/папки', 'дата доступа']
    """
    need_tuple_size = 2
    path_time_part = path_time_part.strip()
    re_value = re.findall(r'(.*)\s+(\w{3}\s+\w{3}\s+[0-9]{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2}\s+\d{4})$', path_time_part)
    try:
        re_value_tuple = re_value[0]
    except IndexError:
        return []

    re_value_size = len(re_value_tuple)
    if re_value_size < need_tuple_size:
        return []

    try:
        path_of_file = re_value_tuple[0]
        time_of_access = re_value_tuple[1]
    except IndexError:
        return []

    path_of_file = path_of_file.rstrip()
    return [path_of_file, time_of_access]


@app.route('/')
def index():
    page_title = 'SambaStatus'
    smb_data = smb_status()
    smb_lines = parse_status(smb_data)
    return render_template('index.html', page_title=page_title, smb_lines=smb_lines)


def main():
    uid_users_dict = make_uid_users_dict()
    print(uid_users_dict)

    smb_data = smb_status()
    smb_lines = parse_status(smb_data, uid_users_dict)


if __name__ == '__main__':
    main()
    # app.run(debug=True)
