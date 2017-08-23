# Python

Python is a general-purpose programming language widely used by data scientists.

If you are not familiar with Python then please consider doing one of the courses below.

## Introduction to Python for the absolute beginner

* <a href="https://www.datacamp.com/courses/intro-to-python-for-data-science" target="_blank">Intro to Python for Data Science</a>
* <a href="https://www.codecademy.com/learn/python" target="_blank">Codecademy Python introduction course</a>

## Practical Python for Astronomers

[Practical Python for Astronomers](https://python4astronomers.github.io/) is a series of hands-on workshops to explore the Python language and the powerful analysis tools it provides. The emphasis is on using Python to solve real-world problems that astronomers are likely to encounter in research.

## Books

Below are a list of books which you may find useful whilst learning to program in Python. They are freely accessible, but make sure you adhere to the licences set forth by the autors. If there are books missing that you would like to add, then fork this repository, add the book and then create a pull request.

 <table style="width:100%">
  <tr>
    <th>Book</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="http://greenteapress.com/wp/think-python/" target="_blank"><img src="http://greenteapress.com/thinkpython/think_python_comp2.medium.png" alt="Think Python" width="200"/></a></td>
    <td><b>Think Python</b><br>Think Python is an introduction to Python programming for beginners. It starts with basic concepts of programming, and is carefully designed to define all terms when they are first used and to develop each new concept in a logical progression. Larger pieces, like recursion and object-oriented programming are divided into a sequence of smaller steps and introduced over the course of several chapters.
	<br>The book is available for download <a href="http://greenteapress.com/wp/think-python/" target="_blank">here</a>.
    </td>
  </tr>
    <tr>
    <td><a href="http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf" target="_blank"><img src="http://covers.oreillystatic.com/images/0636920053194/cat.gif" alt="A Whirlwind Tour of Python " width="200"/></a></td>
    <td><b>A Whirlwind Tour of Python</b><br>To tap into the power of Python's open data science stack—including NumPy, Pandas, Matplotlib, Scikit-learn, and other tools—you first need to understand the syntax, semantics, and patterns of the Python language. This report provides a brief yet comprehensive introduction to Python for engineers, researchers, and data scientists who are already familiar with another programming language.
  <br>The book is available for download <a href="http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf" target="_blank">here</a>.
    </td>
  </tr>
  <tr>
    <td><a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank"><img src="https://github.com/jakevdp/PythonDataScienceHandbook/raw/master/notebooks/figures/PDSH-cover.png" alt="Python Data Science Handbook" width="200"/></a></td>
    <td><b>Python Data Science Handbook</b><br>The book introduces the core libraries essential for working with data in Python: particularly IPython, NumPy, Pandas, Matplotlib, Scikit-Learn, and related packages. Familiarity with Python as a language is assumed; if you need a quick introduction to the language itself, see the free companion project, <a href="https://github.com/jakevdp/WhirlwindTourOfPython" target="_blank">A Whirlwind Tour of Python</a>: it's a fast-paced introduction to the Python language aimed at researchers and scientists.
  <br>The book is available for download <a href="https://github.com/jakevdp/PythonDataScienceHandbook" target="_blank">here</a>.
    </td>
  </tr>
</table> 

A long list of freely accissible Python programming books can be found <a href="https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#python" target="_blank">here</a>.

## Astronomy based Python packages

### Astropy

![Astropy Logo](astropy_banner.jpg?raw=true)

Astropy is a community-driven package intended to contain much of the core functionality and some common tools needed for performing astronomy and astrophysics with Python. To learn more head on over to the [astropy website](http://www.astropy.org/).

### Astroquery

Astroquery is an [astropy](http://www.astropy.org) affiliated package that
contains a collection of tools to access online Astronomical data. Each web
service has its own sub-package. For example, to interface with the [SIMBAD website](http://simbad.u-strasbg.fr/simbad/), use the ``simbad`` sub-package:

```python

    >>> from astroquery.simbad import Simbad
    >>> theta1c = Simbad.query_object('tet01 Ori C')
    >>> theta1c.pprint()
       MAIN_ID          RA           DEC      ... COO_QUAL COO_WAVELENGTH     COO_BIBCODE
    ------------- ------------- ------------- ... -------- -------------- -------------------
    * tet01 Ori C 05 35 16.4637 -05 23 22.848 ...        A              O 2007A&A...474..653V
```

To view the documentation and code head on over to the <a href="https://github.com/astropy/astroquery" target="_blank">Astroquery GitHub page</a>.

### AstroML: Machine Learning code for Astronomy

AstroML is a Python module for machine learning and data mining built on numpy, scipy, scikit-learn, and matplotlib, and distributed under the 3-Clause BSD license. It contains a growing library of statistical and machine learning routines for analyzing astronomical data in python, loaders for several open astronomical datasets, and a large suite of examples of analyzing and visualizing astronomical datasets. To learn more visit the [astroML website](https://pypi.python.org/pypi/astroML).