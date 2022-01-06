from enum import Enum


class EnumChoices(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)

    @classmethod
    def values(cls):
        return [x.value for x in cls]

    @classmethod
    def names(cls):
        return [x.name for x in cls]

    @classmethod
    def get_value(cls, name):
        return getattr(cls, name).value

    @classmethod
    def cls_name(cls):
        return cls.__qualname__

    @classmethod
    def text_value_list(cls):
        data_list = []
        for x in cls:
            data_list.append({"text": x.value, "value": x.name})
        return data_list
