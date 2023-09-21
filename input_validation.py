import email_validator
from re import findall
from email_validator import EmailNotValidError


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    email_validator.CHECK_DELIVERABILITY = False

    try:
        email_validator.validate_email(email, )
        return True

    except EmailNotValidError as e:
        return False


def is_valid_password(password: str) -> bool:
    if type(password) is not str:
        raise TypeError

    pattern_non_word_chars = r'\W'
    has_extra_chars = len(findall(pattern_non_word_chars, password)) > 0

    if len(password) < 8:
        return False

    if len(password) < 25 and not has_extra_chars:
        return False

    return True