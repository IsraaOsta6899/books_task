from sqlalchemy import Enum, inspect


class HarriEnum(object):
    @classmethod
    def as_list(cls):
        _list = []
        for key, value in cls.__dict__.items():
            if not key.startswith("_") and not inspect.isroutine(value):
                _list.append(value)
        return _list

    @classmethod
    def as_enum(cls):
        _list = cls.as_list()
        return Enum(*_list)


class DateTimeFormat:
    ISO_DATE_FORMAT = '%Y-%m-%d'
    ISO_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class MembershipStatus(HarriEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"  

class FineStatus(HarriEnum):
        RETURNED = 'RETURNED'
        NOTRETURNED = 'NOT-RETURNED'