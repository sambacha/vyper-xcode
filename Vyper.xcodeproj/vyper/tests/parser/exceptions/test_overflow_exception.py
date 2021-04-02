import pytest

from vyper import compiler
from vyper.exceptions import OverflowException

fail_list = [
    """
@external
def foo():
    x: int128 = -170141183460469231731687303715884105729 # -2**127 - 1
    """,
    """
@external
def foo():
    x: decimal = -170141183460469231731687303715884105728.0000000001
    """,
    """
@external
def foo():
    x: uint256 = convert(821649876217461872458712528745872158745214187264875632587324658732648753245328764872135671285218762145, uint256)  # noqa: E501
    """,
    """
@external
def overflow2() -> uint256:
    a: uint256 = 2**256
    return a
    """,
]


@pytest.mark.parametrize("bad_code", fail_list)
def test_invalid_literal_exception(bad_code):
    with pytest.raises(OverflowException):
        compiler.compile_code(bad_code)
