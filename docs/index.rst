.. xsgen documentation master file, created by
   sphinx-quickstart on Fri Oct 31 11:35:50 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

xsgens have awesome rates
==========================

xsgen is a tool for computing multi-group neutron cross-section, burnup, and
multiplication factor (k\ :sub:`inf`\ ) as a function of reactor state, which
includes time/fluence, material properties, and reactor geometry.

We use a plugin-based system to allow a flexible approach with respect to
underlying physics engines.

The source code can be found at the `GitHub project site`_.

For a quick install from source, please clone from the official repo::

    git clone git://github.com/bright-dev/xsgen.git
    cd xsgen/
    python setup.py install --user

Now you should be able to run it simply with::

    xsgen


Contents:
---------

**Usage:**

.. toctree::
   :maxdepth: 1

   overview
   install
   usersguide
   plugins
   plugins-module
   api/index

..
   Indices and tables
   ------------------

   * :ref:`genindex`
   * :ref:`modindex`
* :ref:`search`

.. _GitHub project site: https://github.com/bright-dev/xsgen
