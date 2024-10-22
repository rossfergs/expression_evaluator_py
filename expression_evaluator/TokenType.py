import enum


class TokenType(enum.Enum):
    INTEGER = enum.auto()
    OPERATOR = enum.auto()
    OPENPAREN = enum.auto()
    CLOSEPAREN = enum.auto()
