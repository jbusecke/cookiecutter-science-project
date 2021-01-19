import os
import pytest
from subprocess import check_output
from conftest import system_check


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was jinja able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def get_project_name(self):
        if pytest.param.get('project_name'):
            pname = system_check('DrivenData')
        else:
            pname = 'project_name'
        return pname

    def test_project_name(self):
        project = self.path
        name = self.get_project_name()
        assert project.name == name

    def test_author(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--author']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('author_name'):
            assert p == 'DrivenData'
        else:
            assert p == 'Your name (or your organization/company/team)'

    def test_readme(self):
        readme_path = self.path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert 'DrivenData' == next(fin).strip()

    def test_setup(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--version']
        p = check_output(args).decode('ascii').strip()
        assert p == '0.1.0'

    def test_license(self):
        license_path = self.path / 'LICENSE'
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_license_type(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--license']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('open_source_license'):
            assert p == 'BSD-3'
        else:
            assert p == 'MIT'

    # ! Ill deactivate this for now. Have to find a way to parse requirements from setup cfg
    # def test_requirements(self):
    #     reqs_path = self.path / 'requirements.txt'
    #     assert reqs_path.exists()
    #     assert no_curlies(reqs_path)
    #     if pytest.param.get('python_interpreter'):
    #         with open(reqs_path) as fin:
    #             lines = list(map(lambda x: x.strip(), fin.readlines()))
    #         assert 'pathlib2' in lines

    def test_folders(self):
        name = self.get_project_name().lower().replace(' ','_')
        expected_dirs = [
            name,
            name+'/tests',
            'ci',
            'data',
            'data/external',
            'data/interim',
            'data/processed',
            'data/raw',
            # 'docs',
            'notebooks',
            'references',
            'scripts',
        ]

        ignored_dirs = [
            str(self.path),
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        unexpected_dirs = set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)
        assert set(abs_expected_dirs + ignored_dirs) == set(abs_dirs)

