from ASTNode import ASTNode
from TokenType import TokenType
from parser import parse

def evaluate(node: ASTNode) -> int:
    if node.value is not None:
        return node.value

    left_value = evaluate(node.left)
    right_value = evaluate(node.right)
    match node.operator:
        case "*":
            return left_value * right_value
        case "+":
            return left_value + right_value
        case "-":
            return left_value - right_value


def interpret(input_string: str) -> int:
    syntax_tree = parse(input_string)
    return evaluate(syntax_tree)
