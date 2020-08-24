from irish_fbr.check_website import is_open


def test_is_open():
    fail_response = "this string does not include the correct term"
    assert not is_open(fail_response)
