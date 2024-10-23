import enum


class TokenType(enum.Enum):
    INTEGER = enum.auto()
    MULT = enum.auto()
    ADD = enum.auto()
    MINUS = enum.auto()
    OPENPAREN = enum.auto()
    CLOSEPAREN = enum.auto()
    EOE = enum.auto()
