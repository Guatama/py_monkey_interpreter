from enum import Enum


class TokenType(Enum):
    # Special tokens
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literals
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"      # 1343456

    # Operators
    ASSIGN = "="
    PLUS = "+"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"


class Token():
    def __init__(self, token_type: TokenType, literal: str):
        self.type = token_type
        self.literal = literal

    def __str__(self):
        return f"Token({self.type}, {self.literal})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Token):
            return False
        return self.type == value.type and self.literal == value.literal
