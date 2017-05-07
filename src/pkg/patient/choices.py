from enum import Enum


class ChoiceBaseEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple([
            (enum.value, name) for name, enum in
            cls.__members__.items()
        ])


class ChoiceStringEnum(str, ChoiceBaseEnum):
    pass


class ChoiceEnum(int, ChoiceBaseEnum):
    pass


class BloodTypeEnum(ChoiceStringEnum):
    First_positive = '0+'
    First_negative = '0-'

    Second_positive = 'A+'
    Second_negative = 'A-'

    Third_positive = 'B+'
    Third_negative = 'B-'

    Fourth_positive = 'AB+'
    Fourth_negative = 'AB-'


class SexEnum(ChoiceStringEnum):
    male = 'male'
    female = 'female'


class PatientStatus(ChoiceEnum):
    Live = 0
    Hospital = 1
    Dead = 2
