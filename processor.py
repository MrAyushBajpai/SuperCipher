from random import randint
import string


class Keys:
    def __init__(self, value):
        self.Value = value

    def getvalue(self):
        return self.Value

    def setvalue(self, value):
        self.Value = value


def encrypt(data: str, key: Keys):
    data = list(data)
    key_value = Keys.getvalue(key)
    first_list = list(string.printable)
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
    i = 0
    data_length = len(data)
    offset = (average_place_offset % 3) + 1
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
        new_data.append(second_list[first_list.index(i)])

    return ''.join(new_data)


def decrypt(data: str, key: Keys):
    data = list(data)
    key_value = Keys.getvalue(key)
    first_list = list(string.printable)
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
