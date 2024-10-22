from dataclasses import dataclass
import TokenType


@dataclass
class Token:
    symbol: str
    value: TokenType
