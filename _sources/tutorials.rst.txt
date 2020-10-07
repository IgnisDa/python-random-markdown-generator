Tutorials to use this package
==============================

Creating lists using :class:`MarkdownOutputGenerator`
-----------------------------------------------------

An object of :class:`MarkdownOutputGenerator` class provides
:meth:`.add_unordered_list_item`, :meth:`.add_ordered_list_item`,
:meth:`.add_unordered_list` and :meth:`.add_ordered_list` method to add lists
and list items to your generated markdown.

Make sure you import the correct components and initialize them:

.. code-block:: python

    >>> from mdgen import MarkdownOutputGenerator
    >>> markdowngen = MarkdownOutputGenerator()

To create a single unordered list item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> markdowngen.add_unordered_list_item('test unordered list')
    >>> markdowngen.get_output_text()
    '* test unordered list\n'

To create an unordered list
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> markdowngen.add_unordered_list(['list item one', 'two' , 'three'],
    ... style='plus')
    >>> markdowngen.get_output_text()
    '+ list item one\n+ two\n+ three\n'

To create a single ordered list item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> markdowngen.add_ordered_list_item('test ordered list', index=3,
    ... indent=2)
    >>> markdowngen.get_output_text()
    '\t\t3. test ordered list\n'
    >>> markdowngen.add_ordered_list_item('test ordered list')
    >>> markdowngen.get_output_text()
    '\t\t3. test ordered list\n1. test ordered list\n'

To create an ordered list
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> markdowngen.add_ordered_list(['list item one', 'two' , 'three'])
    >>> markdowngen.get_output_text()
    '1. list item one\n1. two\n1. three\n'
    >>> markdowngen.add_ordered_list(['list item one', ('two', 3) , ('three', 2, 1)])
    >>> markdowngen.get_output_text()
    '1. list item one\n1. two\n1. three\n1. list item one\n\t\t\t1. two\n\t\t1. three\n'
    >>> # function usage: .add_ordered_list([('item1', int: indent, int: index), ('item2', int: indent, int: index) ...])
