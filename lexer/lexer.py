from py_monkey.token import Token, TokenType


class Lexer():
    source_code: str
    position: int
    read_position: int
    ch: str

    def __init__(self, source_code: str):
        self.source_code = source_code
        self.position = 0
        self.read_position = 1
        self.ch = source_code[self.position]

    def read_char(self):
        if self.read_position >= len(self.source_code):
            self.ch = ""
        else:
            self.ch = self.source_code[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def next_token(self) -> Token:
        match self.ch:
            case "=":
                tok = Token(TokenType.ASSIGN, self.ch)
            case "+":
                tok = Token(TokenType.PLUS, self.ch)
            case "(":
                tok = Token(TokenType.LPAREN, self.ch)
            case ")":
                tok = Token(TokenType.RPAREN, self.ch)
            case "{":
                tok = Token(TokenType.LBRACE, self.ch)
            case "}":
                tok = Token(TokenType.RBRACE, self.ch)
            case ",":
                tok = Token(TokenType.COMMA, self.ch)
            case ";":
                tok = Token(TokenType.SEMICOLON, self.ch)
            case "":
                tok = Token(TokenType.EOF, "")
            case _:
                tok = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()

        return tok
