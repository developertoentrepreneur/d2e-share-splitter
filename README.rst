Share Splitter
==============

A tool to split shares dynamically

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/cookiecutter/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

What is this project about
--------

Share Splitter is a small framework to help your tartup organize your company shares dynamically. 
Built within the django framework, Share Splitter allows you to:
1. Create users using `django-allauth` with yearly salaries
2. Create contributions (either expenses or time) that will increase the owner shares of the company
3. View the shares distribution

Install
--------

To easily and quickly run this repository locally you will need Docker.
Once docker is up and running in your local machine, the next step is to install requirements, run a db and make migrations. It is all achieved by:
::
  $ make local


Initial setup
--------------

Population database
^^^^^^^^^^^^^^^^^^^^^

* To create a **initial project and admin user**, use this command::

    $ make db-populate

A project called `Pecunia` will be created and an admin user with the following credentials will be created:
* Username: `admin`
* Password: `admin`




Running tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

To run tests, a simple command allows you to do so

::

  $ make test-all




