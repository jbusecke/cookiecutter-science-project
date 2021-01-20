import sys
import pytest
import shutil
from pathlib import Path
from cookiecutter import main
from subprocess import check_output

CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {
        'project_name': 'DrivenData',
        'author_name': 'DrivenData',
        'open_source_license': 'BSD-3-Clause',
        'python_interpreter': 'python'
        }
args2 = {
        'project_name': 'cool_stuff',
        'author_name': 'Marty McFly',
        'open_source_license': 'MIT',
        'python_interpreter': 'python'
}


def system_check(basename):
    platform = sys.platform
    if 'linux' in platform:
        basename = basename.lower()
    return basename


@pytest.fixture(scope='class', params=[{}, args, args2])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp('data-project')
    out_dir = Path(temp).resolve()

    pytest.param = request.param

    print(pytest.param)

    main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir
    )

    pn = pytest.param.get('project_name') or 'project_name'
    
    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    
    args = ['git', 'init', proj]
    p = check_output(args)
    print(p)

    # In order for setuptools_scm to work properly, I need to do a git init in the temp directory

    yield 

    # # cleanup after
    # shutil.rmtree(out_dir)