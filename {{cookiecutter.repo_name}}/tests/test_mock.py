from tmp_mock import mocking_test


def test_mocking_test() -> None:
    """
    Test function for mocking_test() function.

    Asserts that the mocking_test() function returns True.
    """
    assert mocking_test() is True
