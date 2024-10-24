import pytest

from py_monkey.lexer import Lexer
from py_monkey.token import TokenType


@pytest.fixture(scope="module")
def lexer():
    # The fixture creates a lexer for the given input
    source_code = "=+(){},;"
    return Lexer(source_code)


def test_lexer_initialization(lexer):
    # This test ensures the lexer initializes correctly
    # Assert initial positions of the lexer
    assert lexer.position == 0, f"Expected initial position to be 0, got {lexer.position}"
    assert lexer.read_position == 1, f"Expected initial readPosition to be 1, got {lexer.read_position}"

    # Check that the initial character (`ch`) is the first character in the input string
    expected_initial_char = "="
    assert lexer.ch == expected_initial_char, f"Expected initial character to be '{expected_initial_char}', got '{lexer.ch}'"


@pytest.mark.parametrize(
    "expected_type, expected_literal",
    [
        (TokenType.ASSIGN, "="),
        (TokenType.PLUS, "+"),
        (TokenType.LPAREN, "("),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RBRACE, "}"),
        (TokenType.COMMA, ","),
        (TokenType.SEMICOLON, ";"),
        (TokenType.EOF, ""),
    ]
)
def test_next_token(lexer, expected_type, expected_literal):
    # Use the lexer created by the fixture
    tok = lexer.next_token()

    # Assertions to compare actual token type and literal with expected values
    assert tok.type == expected_type, f"Token type wrong. Expected={expected_type}, got={tok.type}"
    assert tok.literal == expected_literal, f"Token literal wrong. Expected={expected_literal}, got={tok.literal}"
