from enum import Enum

class Values(Enum):
    EXECUTIVE = 'executive'
    SENIOR = 'senior'
    JUNIOR = 'junior'
    INTERN = 'intern'

def choices():
    choices_list = []
    for enum in Values:
        choices_list.append((enum.value, enum.name))
    return choices_list

print(choices())