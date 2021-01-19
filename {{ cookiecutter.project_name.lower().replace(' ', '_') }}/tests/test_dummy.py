import pytest
from {{cookiecutter.project_name.lower().replace(' ', '_')}}.dummy import dummy_foo


def test_dummy():
    assert dummy_foo(4) == (4 + 4)
