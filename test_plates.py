from plates import is_valid

def main():
    test_starts_num()
    tests_mid_num()
    tests_character()
    tests_punct()
    test_start_zero()

def test_starts_num():
    assert is_valid("00") == False
    assert is_valid("13") == False
    assert is_valid("3a") == False
    assert is_valid("df") == True

def test_start_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def tests_mid_num():
    assert is_valid("sd93fg") == False
    assert is_valid("sdf32g") == False
    assert is_valid("fsae66") == True

def tests_character():
    assert is_valid("sd") == True
    assert is_valid("s") == False
    assert is_valid("sdfgdf43") == False
    assert is_valid("sdfcv4") == True

def tests_punct():
    assert is_valid("sd?.fg") == False
    assert is_valid("sdf#@g") == False
    assert is_valid("fsae%!") == False

if __name__ == "__main__":
    main()
