import pytest
from {{cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_')}}.dummy_module import dummy_foo


def test_dummy():
    assert dummy_foo(4) == (4 + 4)
