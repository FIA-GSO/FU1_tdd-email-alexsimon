import email_validator
from email_validator import EmailNotValidError


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    email_validator.ALLOW_SMTPUTF8 = True

    try:
        email_validator.validate_email(email)
        return True

    except EmailNotValidError as e:
        return False

