{{cookiecutter.project_name}}
==============================
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }}/workflows/Tests/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }}/actions)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }})
{% if cookiecutter.open_source_license == 'MIT' %}[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}[![License:BSD-3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-lightgray.svg?style=flt-square)](https://opensource.org/licenses/BSD-3-Clause)
{% endif %}[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_name.lower().replace(' ', '_') }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name.lower().replace(' ', '_') }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_name.lower().replace(' ', '_') }}/badge/?version=latest)](https://{{ cookiecutter.project_name.lower().replace(' ', '_') }}.readthedocs.io/en/latest/?badge=latest)
<!-- [![conda-forge](https://img.shields.io/conda/dn/conda-forge/{{ cookiecutter.project_name.lower().replace(' ', '_') }}?label=conda-forge)](https://anaconda.org/conda-forge/{{ cookiecutter.project_name.lower().replace(' ', '_') }}) -->

{{ cookiecutter.description }}

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
