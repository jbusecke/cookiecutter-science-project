# How to build everything that is in this repo from scratch

All the steps below assume you have a repo with <repo> as name on github already.

## Documentation with Readthedocs (RTD) and Sphinx

1. Set up an accont at [RTD](https://readthedocs.org/) and activate your repo.
> I recommend to activate the new feature: [autobuild docs for PR](https://docs.readthedocs.io/en/stable/guides/autobuild-docs-for-pull-requests.html). It makes debugging at the end much easier and you won't have to submit 40 PRs to fix the RTD.

2. Create an conda [environment file]() `environment.yml` in the `docs` folder that contains all necessary packages to build the docs. Here is a minimal example:
```yaml
name: <repo>_docs
dependencies:
  - python
  # Insert your dependencies here
  
  #
  - numpydoc
  - sphinx
  - sphinx_rtd_theme
  - ipython
  - ipykernel # not strictly necessary but this is nice to run notebooks in this env to test
  - pandoc
  - pip
  - pip:
    - docrep<=0.2.7
    - nbsphinx
    - jupyter_client
    - sphinx_pangeo_theme
    - sphinx-copybutton
    - sphinxcontrib-srclinks

```
Build the environment with `conda create env -f docs/environment.yml, and activate it with `conda activate <repo>_docs`

3. Setup the folder structure with `sphinx-quickstart`
4. Populate your docs with `.rst` and `.ipynb` files
5. Set up some additional options in `conf.py`:

  - Activate extensions. This is a list that I commonly use:
    ```
    extensions = [
      "sphinx.ext.autodoc",
      "sphinx.ext.viewcode",
      "sphinx.ext.napoleon",
      "nbsphinx",
      "recommonmark",
      "sphinx.ext.mathjax",
      "sphinx.ext.autosummary",
      "sphinx.ext.extlinks",
      "sphinx.ext.intersphinx",
      "numpydoc",
      "nbsphinx",
      "IPython.sphinxext.ipython_directive",
      "IPython.sphinxext.ipython_console_highlighting",
      "sphinxcontrib.srclinks",
    ]
    ```
  - If you work with notebooks in your docs, its always a good idea to ignore the checkpoints 
    ```
    exclude_patterns = ["_build", "**.ipynb_checkpoints", "Thumbs.db", ".DS_Store"]
    ```
  - The pangeo theme is always nice (but of course up to you!) 
    ```
    html_theme = "pangeo"
    ```
5. Build the first version of the docs locally with `make html` and look at the local docs page with `open _build/html/index.html`
6. One of the crucial parts of a good documumentation is the automatic API page. Just create a new `api.rst` with the following content:
  ```rst
  :mod:`<repo> API`
  ----------------------------

  .. automodule:: <repo>.module
     :members:
     :undoc-members:
     :show-inheritance:
  
  ```
  In order to use this feature locally you will have to install the package from the root directory in the <repo>_docs environment with `pip install -e . --no-deps`. RTD will do this automatically
  
  Then run `make_html` again and you should see a nice autogenerated API page (if you added it to the `toctree`!)

7. Finally you should add this to your `.gitignore` to avoid commiting the local build files:
 ```
 docs/_build
 make.bat
 
 ```
 Then add, commit and push to git!