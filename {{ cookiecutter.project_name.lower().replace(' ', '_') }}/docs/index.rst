.. gcm-filters documentation master file, created by
   sphinx-quickstart on Tue Jan 12 09:24:23 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{cookiecutter.project_name.lower().replace(' ', '_')}}'s documentation!
================================================================================================================================

This is an awesome description of {{cookiecutter.project_name.lower().replace(' ', '_')}}, written in `reStructuredText`_.

You can contribute new sections by either adding a new file (see ``new_section.rst``) or just putting a jupyter notebook
in the ``docs`` folder (see ``new_section_notebook.ipynb``).

In either case, make sure to add an entry in the ``.. toctree::``. Check out ``index.rst`` how it was done for the above examples.

.. toctree::
   :maxdepth: 2

   new_section
   new_section_notebook
   api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
