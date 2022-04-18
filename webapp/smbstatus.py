from webapp.getuserlist import check_uid
from webapp.remote_command import prepare_remote_command, start_shell_command
import re
import webapp.config as config

SKIP_LINES = 4
UID = 1
# Pid          Uid        DenyMode   Access      R/W        Oplock
SIZE_LIST_OF_PART1 = 6
# SharePath   Name   Time
SIZE_LIST_OF_PART2 = 3
PATH_TIME_LIST_SIZE = 2


def smb_status():
    smb_status_command = prepare_remote_command(config.SAMBA_STATUS_COMMAND,
                                                config.SSH_PASS_CMD,
                                                config.SSH_PASSWORD,
                                                config.SSH_CMD,
                                                config.SSH_OPTIONS,
                                                config.SSH_USER,
                                                config.SRC_HOST,
                                                )
    return start_shell_command(smb_status_command)


def parse_status(uid_users_dict):
    """
    # '0:Pid 1:Uid 2:DenyMode 3:Access 4:R_W 5:Op_lock 6:SharePath 7:Name 8:Time 9:LoginName'
    :param uid_users_dict:
    :return:
    """
    smb_data = smb_status()

    list_of_user_names = set()
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
            # Пропуск отрытых ресурсов
            if parsed_line[config.PATH_NAME_INDEX] == '.':
                continue

            username = check_uid(parsed_line[config.USER_ID_INDEX], uid_users_dict)
        except IndexError:
            continue

        parsed_line.append(username)
        list_of_user_names.add(username)
        # print(f'Parsed string: {parsed_line}')
        status_records.append(parsed_line)

    list_of_user_names = sorted(list_of_user_names)
    return status_records, list_of_user_names


def sort_records(records, key):
    try:
        result = sorted(records, key=lambda x: x[key])
    except (IndexError, TypeError):
        return []
    return result


def search_records(records, key, search_word):
    result = []
    for record in records:
        try:
            i = record[key].find(search_word)
            if i != -1:
                result.append(record)
        except (IndexError, KeyError):
            continue
    return result


def search_element(status_records, element, element_value) -> list:
    search_results = []
    for record in status_records:
        record_value = record[element]
        if record_value == element_value:
            search_results.append(record_value)
    return search_results


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
        return []

    part2_list = parse_part2(part2)
    if len(part2_list) < SIZE_LIST_OF_PART2:
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


def main():
    # Получаем результат smbstatus -L
    smb_status_result = smb_status()
    print(smb_status_result)

    # Получаем список пользователей
    # uid_users_dict = make_uid_users_dict()
    # print(uid_users_dict)


if __name__ == '__main__':
    main()
