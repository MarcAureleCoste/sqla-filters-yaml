.. sqla-filters-yaml documentation master file, created by
   sphinx-quickstart on Wed Oct  3 15:19:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============================================
sqla-filters-yaml : Build filter tree from YAML
===============================================

.. image:: https://img.shields.io/pypi/v/sqla-filters-yaml.svg
    :target: https://pypi.org/project/sqla-filters-yaml/

.. image:: https://img.shields.io/pypi/l/sqla-filters-yaml.svg
    :target: https://pypi.org/project/sqla-filters-yaml/

.. image:: https://img.shields.io/pypi/wheel/sqla-filters-yaml.svg
    :target: https://pypi.org/project/sqla-filters-yaml/

.. image:: https://img.shields.io/pypi/pyversions/sqla-filters-yaml.svg
    :target: https://pypi.org/project/sqla-filters-yaml/

.. image:: https://img.shields.io/discord/479781351051100170.svg?logo=discord
    :target: https://discord.gg/eQ4Mtc8

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. warning::
    This project is not ready for production so use it carefully because it's not stable.

YAML Parser
-----------

This parser is used to create a filters tree using a yaml file.

.. _sqla-filters-parser-usage:

Usage
-----

For the example we will take a simple entity like the following:

.. code-block:: python

    class Post(Base):
        p_id = sa.Column(sa.Integer, primary_key=True)
        title = sa.Column(sa.String(100))
        content = sa.Column(sa.String)

        def __str__(self):
            return '{} | {}'.format(self.title, self.content)

and your YAML looks like:

.. code-block:: YAML

    type: or
    data:
    - type: operator
      data:
        attribute: title
        operator: eq
        value: Post_01
    - type: operator
      data:
        attribute: title
        operator: eq
        value: Post_03


you can now use sqla-filter to filter your query and get only post with title
equal to 'Post_01' or 'Post_02'.

.. code-block:: python

    # Create a YAML parser instance
    parser = YAMLFiltersParser(raw_yaml_string)

    # A tree is generated with the YAML received.
    # If you set the YAML the tree is automatically updated.
    print(parser.tree)

    # Now you can filter a query
    query = session.query(Post)
    filtered_query = parser.tree.filter(query)

    # Get the results
    # you can also directly call the `all()` from previous step
    # results = filtered_query = parser.tree.filter(query).all()
    results = query.all()

==================
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
