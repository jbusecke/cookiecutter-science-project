"""This is a template for a test module"""
from {{cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_')}}.dummy_module import dummy_foo


def test_dummy():
    """This is a dummy test"""
    assert dummy_foo(4) == (4 + 4)
