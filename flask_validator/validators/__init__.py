from .general import General
from .date import Date

validators = {
    'required': General.required,
    'max': General.max,
    'min': General.min,
    'alpha': General.alpha,
    'integer': General.is_int,
    'float': General.is_float,
    'alphanumeric': General.alphanumeric,
    'list': General.list,
    'bool': General.boolean,
    'regex': General.regex,
    'date': Date.date,
    'date_after': Date.after,
    'date_after_or_equal': Date.after_or_equal,
    'date_before': Date.before,
    'date_before_or_equal': Date.before_or_equal
}
