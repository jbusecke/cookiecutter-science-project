[![Build Status](https://img.shields.io/github/workflow/status/jbusecke/cookiecutter-science-project/CI?logo=github)](https://github.com/jbusecke/cookiecutter-science-project/actions)

# Cookiecutter Science Project

---------------
_A slim cookiecutter template for reproducible science projects._
---------------


If you want to start a science project fast, but still encourage good coding practices and reproducibility without spending hours on the setup this template is for you.

You have just started with python and learning all the great elements of the stack seems overwhelming? Just follow the quickstart guide and have everything set up to 'level up' seamlessly along the way.

This will enable you to setup a repository like [this](https://github.com/jbusecke/cookiecutter-science-project_demo_repo) in minutes, and you can go right back to populating it with amazing science!

This work is modified from [cookiecutter-data-science](https://drivendata.github.io/cookiecutter-data-science/) with some modifications targeted towards earth scientist, but general enough for other fields aswell.

## Requirements to use the cookiecutter template:
 - A [github](https://github.com/) account.
   - Note that your account must be set up for [authentication via SSH key-pair](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) before initializing repositories using cookiecutter.
 - [Conda package manager](https://conda.io/en/latest/)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

You can install [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) easily with conda.

``` bash
$ conda install -c conda-forge cookiecutter
```

## Quickstart
To start a new project, run:
``` bash
$ cookiecutter https://github.com/jbusecke/cookiecutter-science-project
```
(*this should be run from the location that you want the project folder to live, or you will need to move the directory around later.*)

If you have previously created a package with this template confirm the prompt to redownload the newest version.
The installation dialog will ask for a few inputs:
- `project_name`: The name of the project. This will be used as package name and repository name on github for consistency (whitespaces will be replaced with underscores).
- `author_name`: Your name.
- `github_username`: Your username for [github](https://github.com).
- `description`: A short description of the project for the readme.
- `open_source_license`: Chose a license for your package. Currently available licenses are: "MIT" and "BSD-3-Clause", details can be found [here]().
- `python_interpreter`: Chose your python version. In most cases just press enter to chose python 3.
> Unfortunately there seems to be a bug that does [not allow backspace](https://github.com/audreyr/cookiecutter/issues/875) in cookiecutter on certain platforms. If you make a typo cancel the input `ctrl+c` and start over again.

### Setting up git/github

To initialize a git repository in the folder, navigate to your project folder that was just created and do
```
git init
```

We now want to connect this local repository to a github repo. This can be done directly from the command line using the [Github Command Line Interface](https://github.com/cli/cli#installation). You will have to install it following one of the methods described [here](https://github.com/cli/cli#installation)

Now (from the project root folder) you can simply do:
```shell
gh repo create 
```
and follow the instructions. You might have to authenticate this if you are using it for the first time, but this should all be explained by prompts in the command line. 

> Hint: If you want your repository to be private, you can simply do `gh repo create --private` instead of selecting it from the prompts.

Now all you need to do is commit the files and push them (the remote has already been set by the previous command).


### Configuring the conda environment

Now configure the packages you will need (you can add more later) in the 'environment.yml' file and create a conda environment

```
$ conda env create -f environment.yml
```

That's it for the setup. You can now go ahead and start your scientific analysis with the following steps.

```
cd project_name
conda activate <project_name>
jupyter-lab
```

## How to release your package

To make your software accessible for others you want to package and release it so others can install
it easily. The most common ways to install python packages are [pypi]() and [conda]().

### Pypi
Releasing on pypi is already built into the CI. You only have to follow these 4 simple steps:
1. Get an account on [pypi](https://pypi.org)
2. Enter your username and passwords in the Settings > Secrets Menu of your repository. They need to be named `PIPY_USERNAME` and `PIPY_PASSWORD` respectively (watch the spelling!)
3. Fill out the `classifiers` and `install_requires` fields in `setup.cfg`. This will ensure that any dependencies are installed when your package is installed, and your stuff works right out of the box.
4. Release a new version by clicking on `Releases` in the right sidebar and then `Draft a new release`. 
Thats it! For each new version step 4 is all you need to do to publish!

Now you can install your released version of your package with
```
pip install <yourpackagename>
```

### conda
Instructions coming soon.

## Documentation
The template comes with a fully set up documentation and examples. You can test the docs locally by building the docs conda environment 
```
conda env create -f docs/environment.yml
```
Then activate the environment and navigate to the `docs` folder and build the html documentation
```
make html
```
Finally you can open the documentation with
```
open _build/html/index.html
```

### ReadTheDocs - Documentation built into the CI
To enable that the docs are being built for each release, just head over to [ReadTheDocs](https://readthedocs.org/), link your account with github and link your repository. The only option you need to enable is in `Admin`>`Advanced Settings`>`Default Settings`>`Install Project`.
<!-- https://stackoverflow.com/questions/61163378/readthedocs-sphinx-setuptools-scm-how-to -->
Thats it! Everything else will just work. 
> If you want to have a new version of your docs built for each submitted PR (very helpful when working on the docs themselves), navigate to the project and click `Admin`>`Advanced Settings`>`Build pull requests for this project`.


## Optional "nice to have" features

### Code linting

Coming soon





## Organization and additional features

Your `project_name` folder should look like this:

```
├── setup.py
├── README.md             <- The top-level README for developers using this project.
├── LICENSE
├── environment.yml       <- Conda environment file. Create environment with
│                           `conda env create -f environment.yml`
├── .travis.yml           <- Config file for Travis CI
│
├── references            <- Data dictionaries, manuals, and all other explanatory materials.
│
├── notebooks             <- Jupyter notebooks. Naming convention is a number (for ordering),
│                           the creator's initials, and a short `-` delimited description, e.g.
│                           `1.0-jqp-initial-data-exploration`.
│
├── data
│   ├── interim           <- Small subset datasets needed to reproduce results in notebooks.
│   ├── processed         <- Datasets that were processed from `raw` folder
│   └── raw               <- Immutable raw data. Download from source with a script or link from    
│                            other source (e.g. HPC filesytem)
│
├── ci                    <- Files for continous integration; see travis-ci.com
│
└──  project_name         <- Source code for use in this project.
    ├── __init__.py       <- Makes `project_name` a Python module
    │
    ├── dummy.py          <- Example python module file. These contain your installable functions
    |
    └── tests
        └── test_dummy.py <- Test modules corresponding to your module files.
```

The suggested workflow revolves around a preset folder structure. Combined with a set of rules this eliminates the effort to make decisions about directory structure and organization, freeing up mental energy and making the repository mor intuitive to understand.
Head over to [cookiecutter-data-science](https://drivendata.github.io/cookiecutter-data-science/) for a nice discussion.

Keeping all the elements of your project contained in this structure ensures that you can port the project from your laptop to a cluster or share it easily with other people.

#### Version control with git
The setup has already created a matching github repository([example based on this readme](https://github.com/jbusecke/cookiecutter-science-project_demo_repo)) to your local project folder to get you started.
Just add, commit and push any changes you make regularly to have a backed up history of your project.  

#### `data` folder
Contents of the data folder should not be committed to the github repository (*the data folder can be included to the .gitignore file - scroll the bottom of the .gitignore in the template*) . Ideally a script in `scripts` is used to download publicly available data into the `data/raw` folder. In climate science, some datasets (like large global climate model datasets) might not be available publicly or are simply too large to download quickly. In this case we recommend linking the files (using absolute filepaths) into the `data/raw` folders using a script(which itself should reside in `scripts`).
> No content of `data/raw` should ever be modified manually.

Often the raw data has to be subset, cleaned or preprocessed in some other way. I recommend to maintain a [jupyter notebook]() in `notebooks` which reads data from `data/raw` and writes into `data/processed`.

This method ensures that anyone can reproduce the same results given the identical source data. It is also to a large part self-documenting.

#### `notebook` folder
[jupyter notebook]() are a phenomenal tool. They combine code, notes, math, pictures etc in a single container. They tend to get messy quickly over time.
To keep tidy and presentable notebooks:
- Properly name your notebooks. Pick a format (e.g. '<running_no><author><short_description>.ipynb') and stick to it.
- Keep code in notebooks to a minimum. Ideally you want to have only short code cells to visualize data and refactor larger functions into the projects source code (see below)

#### The source code
A bunch of notebooks with thousands of line of code is not a great way to design reproducible science. Using this template your project turns into an installable python package.

Lets say you start exploring some data and then develop a set of functions to calculate some fancy new way to quantify something, calculated in a function `awesome_diagnostic`.  

Wouldnt it be nice if some other researcher could just install your project and try this new method out on a different dataset?
You can easily move code out of your notebooks into a new python module `project_name/new_module.py`.
When you install your package with
```
$ python setup.py develop
```
you can import your function `awesome_diagnostic` in a notebook with
```python
%load_ext autoreload
%autoreload 2
from project_name.new_module import awesome_diagnostic
```
>The cell magic in the first two lines automatically reloads your function
so that you can make changes to `project_name/new_module.py`, save them, and apply the new function in your notebook without having to reload.

Now the only thing you have to do is write some [unit tests](https://docs.pytest.org/en/latest/), to check that your function behaves the way it is expected. These will help to check if changes you make in the future affect the outputs.

 Organize the test function `test_awesome_diagnostic` in a new test module `project_name/test_new_module.py` (an example is provided as `dummy.py` and `test_dummy.py` in the appropriate folders) to check the output of `awesome_diagnostic`.

Over time you will accumulate test for all of your functions, and you can check if they all pass without errors
```
$ py.test project_name
>>> ============================================ test session starts ============================================
>>> platform darwin -- Python 3.7.3, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
>>> rootdir: /Users/juliusbusecke/Desktop/final_testing/project_name
>>> collected 2 items
>>>
>>> project_name/tests/test_dummy.py .                                                                    [ 50%]
>>> project_name/tests/test_new_module.py .                                                               [100%]
>>>
>>> ========================================= 2 passed in 0.08 seconds ==========================================
```

Some general guidelines for when to migrate your functions from notebook to source code:
- __When you want to use the same function in several notebooks__. No need to copy paste functions and then have two slightly different versions evolve over time. Aim to make your function as general as needed and maintain it in the source code.
- __When functions get to long__. As mentioned before, notebooks should be used for initial testing, exploration and then vizualization of result.
If your function definitions take over the majority of your notebook, refactor and clean them up into the source code.

Now at some point, you might want to use one or several of these functions in another project. This is the time to create a separate toolbox and migrate your code. The great thing is, that all the work is done already. All you have to do is copy the module/function and corresponding test (You did write tests, right?) to the new repository and change the import statements at the beginning of the appropriate notebooks. Thats it!

#### Continous integration
So unit-test seem cool, but do you want to run these tests all the time? Of course you dont!

So head over to [travis](https://travis-ci.com/) and log in with your github account and follow the instructions for activating your github repo.
Its one switch and everything else is already set up!
Now every time you push changes to your repository, travis downloads your package and the dependencies and runs all the tests. This way you can quickly identify if recent changes broke some of your code.

> In order for travis to get all the necessary dependencies we use the `ci/requirements-py37.yml`. This is set up in the same way as `environment.yml`, and you have to make sure that the necessary packages are in both files. Some packages that are purely for interactive work like e.g. `jupyter`, do not need to be included in the `ci/requirements-py37.yml` environment file.

#### General Principals
All the suggestions are just that - suggestions. Feel free to change things around
and experiment until you find the perfect workflow.

I think that generally a set of principles should apply:
- __Avoid repetions__: That means for example to link a datatset into the `data/raw` folder and read it in several notebooks with something like `xr.open_dataset('../data/raw/dataset.nc')` or to refactor and generalize functions into the source code and import it into notebooks as needed, instead of keeping very similar or copied function definition in each notebook.
- __Document as you go__: You will rarely do it afterwards, and if that happens it will be a pain! When you develop a function you usually write little snippets of code to test it out. Take the extra time to convert them into unittests. Test are a great way of documenting what functions are supposed to do! The same principal applies to other documentation. If you can structure data the way that it is self-explanatory, that helps more than a long README (but also write the README to get people started please!).
Use your notebooks to present results without code ([example](https://github.com/jbusecke/guides/blob/master/analysis_sharing_workflow.md)), instead of writing up the same passages in an email with a bunch of loose figures. Your collaborators/advisors/mum will thank you!

If you have suggestions, feel free to raise an issue or submit a pull request.

Until then SCIENCE ON!

![](https://media.giphy.com/media/LXr2Uxk2xUO2I/giphy.gif)


## Developer notes

The template has some rudimentary tests, but in order to test a PR/branch in a real world scenario, I currently submit the PR and then check out the corresponding branch with:
```shell
cookiecutter https://github.com/jbusecke/cookiecutter-science-project --checkout <pr_branch>
```

That way I can test the full workflow including setting up a github repo and pushing to there.
