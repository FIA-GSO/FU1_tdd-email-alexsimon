import pytest
from input_validation import is_valid_email

@pytest.mark.parametrize("email", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
,   ("test@email.co.uk")
,   ("te-st@email.com")
,   ("te_st@email.com")
,   ("test1@email.com")
,   ("email@[123.123.123.123]")
,   ("email@123.123.123.123")
,   ("firstname+lastname@example.com")
,   ("1234567890@example.com")
,   ("_______@example.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email")      # Fehlende Top-Level-Domain
,   ("test@em@ail.com") # Mehrfaches @-Zeichen
,   ("Abc..123@example.com")
,   ("あいうえお@example.com")
,   ("email@111.222.333.44444")
,   ("Joe Smith <email@example.com>")
,   ("email..email@example.com")
])
def test_is_valid_email__ungueltige_Adressen(email):
    # act
    response = is_valid_email(email)
    
    # assert
    assert response is False