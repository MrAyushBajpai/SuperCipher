import os.path
from random import randint
from string import printable


def encrypt(data: str, key_value: str):
    data = list(data)
    first_list = list(printable)
    first_list = first_list[:95]
    second_list = first_list

    place_offset = 0
    for i in key_value:
        place_offset += ord(i)

    left_place_offset = 0
    for i in key_value[:len(key_value) // 2]:
        left_place_offset += ord(i)

    right_place_offset = 0
    for i in key_value[len(key_value) // 2:]:
        right_place_offset += ord(i)

    average_place_offset = place_offset // len(key_value)
    data_length = len(data)
    offset = (average_place_offset % 3) + 1
    i = 0
    while i < data_length:
        data.insert(i, chr(randint(33, 125)))
        i += offset
        if offset != 1:
            data_length += 1

    data = [data[(i + place_offset) % len(data)]
            for i, x in enumerate(data)]

    first_list = [first_list[(i + left_place_offset) % len(first_list)]
                  for i, x in enumerate(first_list)]

    second_list = [second_list[(i + right_place_offset) % len(second_list)]
                   for i, x in enumerate(second_list)]

    new_data = []
    for i in data:
        if i in '\n\t\r\x0b\x0c':
            new_data.append(i)
        else:
            new_data.append(second_list[first_list.index(i)])

    return ''.join(new_data)


def decrypt(data: str, key_value: str):
    data = list(data)
    first_list = list(printable)
    first_list = first_list[:95]
    second_list = first_list

    place_offset = 0
    for i in key_value:
        place_offset += ord(i)

    left_place_offset = 0
    for i in key_value[:len(key_value) // 2]:
        left_place_offset += ord(i)

    right_place_offset = 0
    for i in key_value[len(key_value) // 2:]:
        right_place_offset += ord(i)

    average_place_offset = place_offset // len(key_value)

    first_list = [first_list[(i + left_place_offset) % len(first_list)]
                  for i, x in enumerate(first_list)]

    second_list = [second_list[(i + right_place_offset) % len(second_list)]
                   for i, x in enumerate(second_list)]

    new_data = []
    for i in data:
        if i in '\n\t\r\x0b\x0c':
            new_data.append(i)
        else:
            new_data.append(first_list[second_list.index(i)])

    new_data = [new_data[(i - place_offset) % len(new_data)]
                for i, x in enumerate(new_data)]

    offset = (average_place_offset % 3) + 1
    i = 0
    while i < len(new_data):
        new_data[i] = 'DELETE'
        i += offset
    data = [i for i in new_data if i != 'DELETE']

    return ''.join(data)
