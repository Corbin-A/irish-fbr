from irish_fbr.check_website import is_open


def test_is_open():
    assert not is_open(
        "Please note that we have stopped processing Foreign Birth Registrations"
    )

    fail_response = "We're open for business!"
    assert is_open(fail_response)
