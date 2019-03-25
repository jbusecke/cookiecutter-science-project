# Cookiecutter Science Project

_A slim cookiecutter template for science projects._


Inspired by [cookiecutter-science-project](https://github.com/jbusecke/cookiecutter-science-project)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda - c conda-forge install cookiecutter
```


### To start a new project, run:
------------
``` bash
$ cookiecutter https://github.com/jbusecke/cookiecutter-science-project
```
If you have previously created a package with this template confirm the prompt to redownload the newest version.
The installation dialog will ask for a few inputs:
- `project_name`: The name of the project. This will be used as package name and repository name on github for consistency (whitespaces will be replaced with underscores)
-



The directory includes a simple setup script, which will create a github repository and commit the current state as initial commit.

In the directory created by cookiecutter do

```bash
$ ./scripts/setup.sh
```

Now head over to [travis](https://travis-ci.org/), ...
For each service log in with your github account and follow the instructions for activating your github repo.
> It can take a while until new repos show up in travis. Just get a cup of coffee or have a nice chat with your office mate.

You can check if everything is working properly by committing some text to the readme, or just get straight to analysis!





<!-- ### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing). -->

<!-- ### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests -->
