{{cookiecutter.project_name}}
==============================
[![Build Status](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }})
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name.lower().replace(' ', '_') }})
{% if cookiecutter.open_source_license == 'MIT' %}[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}[![License:BSD-3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-lightgray.svg?style=flt-square)](https://opensource.org/licenses/BSD-3-Clause)
{% endif %}

{{ cookiecutter.description }}

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
