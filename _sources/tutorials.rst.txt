Tutorials to use this package
==============================

Creating lists using :class:`MarkdownOutputGenerator`
-----------------------------------------------------

An object of :class:`MarkdownOutputGenerator` class provides
:meth:`.add_unordered_list_item`, :meth:`.add_ordered_list_item`,
:meth:`.add_unordered_list` and :meth:`.add_ordered_list` method to add lists
and list items to your generated markdown.

.. code-block:: python

    >>> from mdgen import MarkdownOutputGenerator
    >>> markdowngen = MarkdownOutputGenerator()
    >>> markdowngen.add_unordered_list_item('test unordered list')
