# Python

Python is a general-purpose programming language widely used by data scientists.

If you are not familiar with Python then please consider doing one of the courses below.

## Introduction to Python for the absolute beginner

* <a href="https://www.datacamp.com/courses/intro-to-python-for-data-science" target="_blank">Intro to Python for Data Science</a>
* <a href="https://www.codecademy.com/learn/python" target="_blank">Codecademy Python introduction course</a>

## Astropy

![Astropy Logo](astropy_banner.jpg?raw=true)

Astropy is a community-driven package intended to contain much of the core functionality and some common tools needed for performing astronomy and astrophysics with Python.

## Accessing Online Astronomical Data

### Acquiring astronomical data using Astroquery

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