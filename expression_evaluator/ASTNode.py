from dataclasses import dataclass
from __future__ import annotations


@dataclass
class ASTNode:
    value: int
    left: ASTNode = None
    right: ASTNode = None