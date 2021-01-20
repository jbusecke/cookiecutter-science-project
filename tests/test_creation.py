import os
import sys
import pytest
from subprocess import check_output
from conftest import system_check

from sys import platform

if 'win32' == platform and sys.version.split(' ')[0] < '3.8':
    pytestmark = pytest.mark.skip('Something doesnt work with windows paths for python <3.8')

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
            pname = pytest.param.get('project_name')
        else:
            pname = 'project_name'
        return system_check(pname)

    def test_project_name(self):
        project = self.path
        name = self.get_project_name()
        assert project.name == name


# Same problem as below. When I manually go to the folder and execute `python setup.py --author` it works,
# but something here goes wrong...
    # def test_author(self):
    #     root = self.path
    #     setup_ = root.joinpath('setup.py')
    #     print(root)
    #     args = ['python',setup_, '--author']
    #     print(args)
    #     print(os.listdir(self.path))
    #     print(os.listdir(root))
    #     cmd = ' '.join([str(a) for a in args])
    #     cmd = 'cd '+ str(self.path) +' ; python setup.py --author ; cd - ;'
    #     print(cmd)
    #     p = check_output(cmd.split(' '))
    #     print(p)
    #     p = p.decode('ascii').strip()
    #     if pytest.param.get('author_name'):
    #         assert p == pytest.param.get('author_name')
    #     else:
    #         assert p == 'UNKNOWN'

    def test_readme(self):
        readme_path = self.path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert pytest.param.get('project_name') == next(fin).strip()

# and again the same problem... Ill try to address this in a sepera;t
    # def test_setup(self):
    #     setup_ = self.path / 'setup.py'
    #     args = ['python', setup_, '--version']
    #     p = check_output(args).decode('ascii').strip()
    #     assert p == '0.0.0'

    def test_license(self):
        license_path = self.path / 'LICENSE.txt'
        assert license_path.exists()
        assert no_curlies(license_path)

    # I am having consistent problems with these system commands and pytest....
    # 
    # def test_license_type(self):
    #     setup_ = self.path / 'setup.py'
    #     args = ['python', setup_, '--license']
    #     p = check_output(args).decode('ascii').strip()
    #     if pytest.param.get('open_source_license') == 'MIT':
    #         assert p == 'MIT'
    #     elif pytest.param.get('open_source_license') == "BSD-3-Clause":
    #         assert p == 'BSD-3'
    #     else:
    #         assert p == 'UNKNOWN' # no input defaults to MIT
            

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
            '.github',
            '.github/workflows',
            '.github/workflows/optional',
            'tests',
            'ci',
            'data',
            'data/external',
            'data/interim',
            'data/processed',
            'data/raw',
            # 'docs',
            'notebooks',
        ]

        ignored_dirs = [
            str(self.path),
            str(self.path)+'/.git',
            str(self.path)+'/.git/info',
            str(self.path)+'/.git/objects',
            str(self.path)+'/.git/objects/pack',
            str(self.path)+'/.git/objects/info',

            str(self.path)+'/.git/refs',
            str(self.path)+'/.git/refs/heads',
            str(self.path)+'/.git/refs/tags',

            str(self.path)+'/.git/hooks',
     
            str(self.path)+'/tests/__pycache__',
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        # remove dirs that should be ignored, dont do anything if they dont exist.
        abs_dirs_select = set(abs_dirs) - set(ignored_dirs)
    
        assert set(abs_expected_dirs) == set(abs_dirs_select)


