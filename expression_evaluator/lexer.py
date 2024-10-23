from Token import Token
from TokenType import TokenType
from error import LexerError


def end_of_expression(ch: str) -> bool:
    match ch:
        case ' ' | '\n' | '\t' | '\r':
            return True
        case _:
            return False


def skip_whitespace(input_string: str, idx: int) -> int:
    while input_string[idx] == " ":
        idx += 1
    return idx


def collect_integer_token(input_string: str, idx: int) -> tuple[Token, int]:
    num_literal = ""
    while '0' <= input_string[idx] <= '9':
        num_literal += input_string[idx]
        idx += 1

    return Token(num_literal, TokenType.INTEGER), idx-1


def lex(input_string: str, idx: int) -> tuple[Token, int]:
    if input_string[idx] == " ":
        idx = skip_whitespace(input_string, idx)
    ch = input_string[idx]
    if '0' <= ch <= '9':
        return collect_integer_token(input_string, idx)
    elif ch == '(':
        return Token(ch, TokenType.OPENPAREN), idx
    elif ch == ')':
        return Token(ch, TokenType.CLOSEPAREN), idx
    elif ch == '*':
        return Token(ch, TokenType.MULT), idx
    elif ch == '+':
        return Token(ch, TokenType.ADD), idx
    elif ch == '-':
        return Token(ch, TokenType.MINUS), idx
    else:
        LexerError(f"Unrecognised character: {ch}")
