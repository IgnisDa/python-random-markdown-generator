from typing import List, Tuple

from mdgen.constants import LINESEPARATOR
from mdgen.core import (MarkdownBlockQuoteGenerator, MarkdownBoldGenerator,
                        MarkdownCodeGenerator, MarkdownHeaderGenerator,
                        MarkdownHorizontalRuleGenerator,
                        MarkdownImageGenerator, MarkdownItalicGenerator,
                        MarkdownLinkGenerator, MarkdownListGenerator,
                        MarkdownTableGenerator, MarkdownTextGenerator)


class MarkdownGenerator:

    """ This is the core class that is used to generate markdown text.
    You probably don't want to use this class, unless you are extending
    it somehow. """

    def new_linebreak(self):
        """
        Just returns a new line separator which can be
        used for linebreaks.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_linebreak()
            '\\n'

        """
        return LINESEPARATOR

    def new_text(self, text: str):
        """
        Returns the :code:`text` as it is.

        :param text: A string that will be returned as it is

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_text('This is a test text')
            'This is a test text'

        """

        text_output = MarkdownTextGenerator()
        return text_output.new_text(text)

    def new_text_line(self, text: str):
        """
        Returns a new text line, and adds a linebreak to its end.

        :param text: A string that will be returned with a linebreak appended

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_text_line('This is a test text line')
            'This is a test text line\\n'

        """
        text_line = MarkdownTextGenerator()
        return text_line.new_text_line(text)

    def new_header(self, text: str, header_level: int = 1, linebreak=True, atx=True):
        """
        Returns a markdown header, using :code:`text` and :code:`header_level`, adds a
        linebreak to it (default behavior can be changed using
        `linebreak=False`). Smaller the :code:`header_level`, larger the header.

        :param text: A string that will be used to create the header
        :param header_level: Smaller the `header_level`, larger the header.
        :param linebreak: If a linebreak would be added to the output
        :param atx:  https://google.github.io/styleguide/docguide/style.html#headings

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_header('This is a test header', 2)
            '## This is a test header\\n'

        """
        if not isinstance(header_level, (int,)):
            raise AttributeError(f"`header_level` must be an instance of or {int}")
        if not isinstance(linebreak, (bool,)):
            raise AttributeError(f"`linebreak` must be an instance of or {bool}")
        if not isinstance(atx, (bool,)):
            raise AttributeError(f"`atx` must be an instance of or {bool}")
        header = MarkdownHeaderGenerator(atx)
        return header.new_header(text, header_level, linebreak)

    def new_bold_text(self, text: str):
        """
        Returns the :code:`text` bolded.

        :param text: A string that will be returned as bold text

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_bold_text('This is a test')
            '**This is a test**'

        """
        bold_text = MarkdownBoldGenerator()
        return bold_text.new_bold_text(text)

    def new_italic_text(self, text: str, underscore=True):
        """
        Returns the :code:`text` in italics.

        :param text: A string that will be returned as italic text

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_italic_text('This is a test')
            '_This is a test_'

        """
        if not isinstance(underscore, (bool,)):
            raise AttributeError(f"`underscore` must be an instance of or {bool}")
        italic_text = MarkdownItalicGenerator()
        return italic_text.new_italic_text(text, underscore)

    def new_bold_and_italic_text(self, text: str, underscore=True):
        """
        Returns the :code:`text` bolded and italic.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_bold_and_italic_text('This is a test')
            '_**This is a test**_'

        """
        if not isinstance(underscore, (bool,)):
            raise AttributeError(f"`underscore` must be an instance of {bool}")
        bolded = self.new_bold_text(text)
        return self.new_italic_text(bolded, underscore)

    def new_horizontal_rule(self, style: str = 'hyphens'):
        """
        Returns a markdown horizontal line used to separate sections.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_horizontal_rule()
            '---\\n'

        """
        permitted_styles = ['hyphens', 'asterisks', 'underscores']
        if style not in permitted_styles:
            raise AttributeError(f"{style} must be among {permitted_styles}")
        horizontal_rule = MarkdownHorizontalRuleGenerator()
        return horizontal_rule.new_horizontal_rule(style)

    def new_paragraph(self, text: str, paragraph_size: int = 79):
        """
        Returns a markdown paragraph, each line formatted to contain
        :code:`paragraph_size` characters each. Defaults to 79.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_paragraph('hello this is an epic paragraph', 12)
            'hello this is an \\nepic paragraph \\n'

        """
        paragraph = MarkdownTextGenerator(paragraph_size)
        return paragraph.new_paragraph(text)

    def new_unordered_list_item(self, text: str, indent: int = 0, style: str = 'asterisk'):
        """
        Returns a single unordered markdown list item. an asterisk will be
        prepended by deafult, can be changed by passing :code:`style` argument.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_unordered_list_item('hello')
            '* hello'

        """
        permitted_styles = ['asterisk', 'plus', 'minus']
        if style not in permitted_styles:
            raise AttributeError(f"`{style}` must be among {permitted_styles}")
        list_item = MarkdownListGenerator(style)
        return list_item.new_unordered_list_item(text, indent)

    def new_unordered_list(self, list_items_list: list, style: str = 'asterisk',
                           linebreak: bool = True):
        """
        Returns a markdown list of unordered list. :code:`list_items_list` must be a
        list of lists (or tuples).

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_unordered_list(['hello', 'hi', 'how do you do?', ('sup', 2)])
            '* hello\\n* hi\\n* how do you do?\\n\\t\\t* sup\\n'
            >>> m.new_unordered_list([('hello', 1), 'hi', 'how do you do?', ('sup', 2)])
            '\\t* hello\\n* hi\\n* how do you do?\\n\\t\\t* sup\\n'

        """

        output = ''
        for list_item in list_items_list:
            if isinstance(list_item, (List, Tuple)):
                output += (f"{self.new_unordered_list_item(*list_item, style=style)}"
                           f"{LINESEPARATOR}")
            else:
                output += (f"{self.new_unordered_list_item(list_item, style=style)}"
                           f"{LINESEPARATOR}")
        if not linebreak:
            output = output[:-1]
        return output

    def new_ordered_list_item(self, text: str, indent: int = 0, index: int = 1):
        """
        Returns a single ordered markdown list item. :code:`index` will be the
        number prepended, and if not supplied, defaults to 1.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_ordered_list_item('hello', indent=2)
            '\\t\\t1. hello'

        """
        list_item = MarkdownListGenerator()
        return list_item.new_ordered_list_item(text, indent, index)

    def new_ordered_list(self, list_items_list: list, linebreak: bool = True):
        """
        Returns a markdown list of ordered list. :code:`list_items_list` must be a
        list of lists (or tuples).

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_ordered_list([('hello', 1, 3), 'hi', 'how do you do?', ('sup', 2)])
            '\\t3. hello\\n1. hi\\n1. how do you do?\\n\\t\\t1. sup\\n'

        """
        output = ''
        for list_item in list_items_list:
            if isinstance(list_item, (List, Tuple)):
                output += f"{self.new_ordered_list_item(*list_item)}{LINESEPARATOR}"
            else:
                output += f"{self.new_ordered_list_item(list_item)}{LINESEPARATOR}"
        if not linebreak:
            output = output[:-1]
        return output

    def new_table(self, list_items_list: list):
        """
        Returns a markdown table. :code:`list_items_list` must be a list of list
        (or tuples).

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> table_data = [['hello', 'hi', 'how do you do?'], ['1', '2', '3', '4']]
            >>> markdown_table = m.new_table(table_data)
            >>> markdown_table
            '|hello|hi|how do you do?|\\n|-----|--|--------------|\\n|1|2|3|4|\\n'

        """
        table = MarkdownTableGenerator()
        return table.new_table(list_items_list)

    def new_link(self, link_text: str, link_url: str = '', linebreak: bool = False):
        """
        Returns a markdown link which can be used to link external websites, or
        even internal ones. If :code:`link_url` is not provided, an empty link is
        returned.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_link('Visit this link')
            '[Visit this link]()'
            >>> m.new_link('Visit this link', 'http://shadyUrl.com/')
            '[Visit this link](http://shadyUrl.com/)'

        """
        link = MarkdownLinkGenerator()
        return link.new_link(link_text, link_url, linebreak)

    def new_comment(self, comment_text: str):
        """ Returns the :code:`comment_text` within markdown comment blocks.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_comment('This is a comment')
            '<!-- This is a comment -->'

        """
        comment_output = MarkdownTextGenerator()
        return comment_output.new_comment(comment_text)

    def new_image(self, alt_text: str, image_url: str, image_title: str = ''):
        """
        Returns a markdown link which can be used to link external websites, or
        even internal ones. If :code:`link_url` is not provided, an empty link is
        returned.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_image('image one', 'http://example.org/?image=one')
            '![image one](http://example.org/?image=one)'
            >>> m.new_image('image two', 'http://example.org/?image=second',
            ... 'The 2nd image')
            '![image two](http://example.org/?image=second "The 2nd image")'

        """
        image = MarkdownImageGenerator()
        return image.new_image(alt_text, image_url, image_title)

    def new_code_block(self, code: str, language: str = 'python'):
        """
        Returns a markdown code block. Valid languages for code formatting
        at: https://github.com/github/linguist/blob/master/lib/linguist/languages.yml

        :param code: A string containing the code-block to be generated
        :param language: The language that the code-block will use

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> code = \"\"\"\\
            ... import os
            ... print(os.uname())\\
            ... \"\"\"
            >>> output = m.new_code_block(code, language="python")
            >>> print(output)
            ```python
            import os
            print(os.uname())
            ```

        """
        code_block = MarkdownCodeGenerator()
        return code_block.new_code_block(code, language)

    def new_blockquote(self, quote: str):
        """
        Returns a markdown blockquote.

        :param quote: A string containing the quote to be generated

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_blockquote('What the heck guys???')
            '> What the heck guys???'

        """
        quote_to_add = MarkdownBlockQuoteGenerator()
        return quote_to_add.new_blockquote(quote)
