"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):

    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:

    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:

    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:

    return id(first) == id(second)


def multiple_ints(first_value: int, second_value: int) -> int:

    if not type(first_value) is int or not type(second_value) is int:
        raise TypeError("Type Error")
    else:
        return first_value * second_value


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:

    try:
        first_value = int(first_value)
        second_value = int(second_value)
        return first_value * second_value
    except TypeError:
        print("Some Error occured")


def is_word_in_text(word: str, text: str) -> bool:

    text_list = text.split()
    LEN = len(text_list)
    counter = len(text_list) - 1

    for i in range(LEN):
        if word == text_list[i]:
            break
        elif word != text_list[i]:
            if counter == 0:
                return False
            counter = counter - 1
            continue
    return True


def some_loop_exercise() -> list:

    some_list = []
    for i in range(0, 13):
        if i == 6 or i == 7:
            continue
        some_list.append(i)
    return some_list



def remove_from_list_all_negative_numbers(data: List[int]) -> list:

    # new_data = []
    # for i in range(len(data)):
    #     if data[i] > 0:
    #         new_data.append(data[i])
    # return new_data

    while min(data) <= 0:
        LEN = len(data)
        counter = 1
        for i in range(LEN):
            if data[i] <= 0:
                data.remove(data[i])
                counter = counter + 1
            if i >= LEN - counter:
                break
        if data == []:
            break
    return data

def alphabet() -> dict:
    """
    Create dict which keys are alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    letters = ["a", "b", "c", "d", "e",
               "f", "g", "h", "i", "j",
               "k", "l", "m", "n", "o",
               "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y",
               "z"]
    alphabet_dict = {}
    for i in range(len(letters)):
        alphabet_dict[i + 1] = letters[i]
    return alphabet_dict


def simple_sort(data: List[int]) -> List[list]:

    new_data = []
    for i in range(len(data)):
        new_data.append(min(data))
        data.remove(min(data))
        data.append(max(data))
    return new_data