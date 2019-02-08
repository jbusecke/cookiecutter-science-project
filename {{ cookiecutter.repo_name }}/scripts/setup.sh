#!bin/bash
# Link local repository to git (you need to create a github repo with the
# same name before)
git init
git add *
git add .gitignore *.yml
git commit -m 'first commit'
git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
git push -u origin master
