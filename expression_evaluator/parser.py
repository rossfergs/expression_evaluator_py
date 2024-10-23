from error import ParseError
from ASTNode import ASTNode
from TokenType import TokenType
from lexer import lex


def parse(input_string: str) -> ASTNode:
    start_node = ASTNode()

    def parse_operator(current_node: ASTNode, current_idx: int) -> tuple[bool, int]:
        token, current_idx = lex(input_string, current_idx)
        if token.value == TokenType.ADD:
            current_node.operator = "+"
        elif token.value == TokenType.MINUS:
            current_node.operator = "-"
        elif token.value == TokenType.MULT:
            current_node.operator = "*"
        else:
            ParseError("Invalid operator")
            return False, current_idx
        return True, current_idx

    def parse_expression(current_node: ASTNode, current_idx: int) -> tuple[bool, int]:
        token, current_idx = lex(input_string, current_idx)
        if token.value == TokenType.INTEGER:
            current_node.value = int(token.symbol)
            return True, current_idx

        if token.value == TokenType.OPENPAREN:
            current_node.left = ASTNode()
            left_result, current_idx = parse_expression(current_node.left, current_idx+1)
            if not left_result:
                ParseError("Invalid expression on left of operator")

            oper_result, current_idx = parse_operator(current_node, current_idx+1)
            if not oper_result:
                ParseError("Invalid operator")

            current_node.right = ASTNode()
            right_result, current_idx = parse_expression(current_node.right, current_idx+1)
            if not right_result:
                ParseError("Invalid expression on right of operator")

            current_idx += 1
            token, current_idx = lex(input_string, current_idx)
            if token.value != TokenType.CLOSEPAREN:
                ParseError("Unclosed parenthesis")
                return False, current_idx

            return True, current_idx

    parse_expression(start_node, 0)
    return start_node
