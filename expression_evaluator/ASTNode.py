from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ASTNode:
    value: int = None
    operator: str = None
    left: ASTNode = None
    right: ASTNode = None
