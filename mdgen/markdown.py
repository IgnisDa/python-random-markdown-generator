from mdgen.constants import LINESEPARATOR
from mdgen.core import (MarkdownBoldGenerator, MarkdownHeaderGenerator,
                        MarkdownHorizontalRuleGenerator,
                        MarkdownImageGenerator, MarkdownItalicGenerator,
                        MarkdownLinkGenerator, MarkdownListGenerator,
                        MarkdownTableGenerator, MarkdownTextGenerator)


class MarkdownGenerator:

    """ This is the core class that is used to generate markdown text.
    You probably don't want to use this class, unless you are extending
    it somehow. """

    def new_text(self, text: str):
        """
        Returns the `text` as it is.

        :param text: A string that will be returned as it is

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_text('This is a test text')
            'This is a test text'

        """

        text_output = MarkdownTextGenerator()
        output = text_output.new_text(text)
        return output

    def new_text_line(self, text: str):
        """
        Returns a new text line, and adds a linebreak to its end.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_text_line('This is a test text line')
            'This is a test text line\\n'

        """
        text_line = MarkdownTextGenerator()
        output = text_line.new_text_line(text)
        return output

    def new_header(self, text: str, header_level: int = 1, linebreak=True, atx=True):
        """
        Returns a markdown header, using `text` and `header_level`, adds a
        linebreak to it (default behavior can be changed using
        `linebreak=False`). Smaller the `header_level`, larger the header.

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
        output = header.new_header(text, header_level, linebreak)
        return output

    def new_bold_text(self, text: str):
        """
        Returns the `text` bolded.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_bold_text('This is a test')
            '**This is a test**'

        """
        bold_text = MarkdownBoldGenerator()
        output = bold_text.new_bold_text(text)
        return output

    def new_italic_text(self, text: str, underscore=True):
        """
        Returns the `text` in italics.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_italic_text('This is a test')
            '_This is a test_'

        """
        if not isinstance(underscore, (bool,)):
            raise AttributeError(f"`underscore` must be an instance of or {bool}")
        italic_text = MarkdownItalicGenerator()
        output = italic_text.new_italic_text(text, underscore)
        return output

    def new_bold_and_italic_text(self, text: str, underscore=True):
        """
        Returns the `text` bolded and italic.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_bold_and_italic_text('This is a test')
            '_**This is a test**_'

        """
        if not isinstance(underscore, (bool,)):
            raise AttributeError(f"`underscore` must be an instance of or {bool}")
        bolded = self.new_bold_text(text)
        bolded_and_italic = self.new_italic_text(bolded, underscore)
        return bolded_and_italic

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
            raise AttributeError(f"`style` must be among {permitted_styles}")
        horizontal_rule = MarkdownHorizontalRuleGenerator()
        output = horizontal_rule.new_horizontal_rule(style)
        return output

    def new_paragraph(self, text: str, paragraph_size: int = 79):
        """
        Returns a markdown paragraph, each line formatted to contain
        `paragraph_size` characters each. Defaults to 79.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_paragraph('hello this is an epic paragraph', 12)
            'hello this is an \\nepic paragraph \\n'

        """
        paragraph = MarkdownTextGenerator(paragraph_size)
        output = paragraph.new_paragraph(text)
        return output

    def new_unordered_list_item(self, text: str, style: str = 'asterisk'):
        """
        Returns a single unordered markdown list item. an asterisk will be
        prepended by deafult, can be changed by passing `style` argument.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_unordered_list_item('hello')
            '* hello'

        """
        permitted_styles = ['asterisk', 'plus', 'minus']
        if style not in permitted_styles:
            raise AttributeError(f"`style` must be among {permitted_styles}")
        list_item = MarkdownListGenerator(style)
        output = list_item.new_unordered_list_item(text)
        return output

    def new_ordered_list_item(self, text: str, index: int = 1):
        """
        Returns a single ordered markdown list item. `index` will be the
        number prepended, and if not supplied, defaults to 1.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_ordered_list_item('hello')
            '1. hello'

        """
        list_item = MarkdownListGenerator()
        output = list_item.new_ordered_list_item(text, index)
        return output

    def new_unordered_list(self, list_items_list: list, style: str = 'asterisk',
                           linebreak: bool = True):
        """
        Returns a markdown list of unordered list. `list_items_list` must be a
        list of lists (or tuples).

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_unordered_list(['hello', 'hi', 'how do you do?'])
            '* hello\\n* hi\\n* how do you do?\\n'

        """
        output = ''
        # indent = 0

        for list_item in list_items_list:
            output += (f"{self.new_unordered_list_item(list_item, style)}"
                       f"{LINESEPARATOR}")
        if not linebreak:
            output = output[:-1]
        return output

    def new_ordered_list(self, list_items_list: list, linebreak: bool = True):
        """
        Returns a markdown list of ordered list. `list_items_list` must be a
        list of lists (or tuples).

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_ordered_list(['hello', 'hi', 'how do you do?'])
            '1. hello\\n2. hi\\n3. how do you do?\\n'

        """
        output = ''
        for index, list_item in enumerate(list_items_list, 1):
            output += self.new_ordered_list_item(list_item, index)
            output += LINESEPARATOR
        if not linebreak:
            output = output[:-1]
        return output

    def new_table(self, list_items_list: list):
        """
        Returns a markdown table. `list_items_list` must be a list of list
        (or tuples).

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_table([['hello', 'hi', 'how do you do?'], ['1', '2', '3', '4']])
            '|hello|hi|how do you do?|\\n|-----|--|--------------|\\n|1|2|3|4|\\n'

        """
        table = MarkdownTableGenerator()
        output = table.new_table(list_items_list)
        return output

    def new_link(self, link_text: str, link_url: str = '', linebreak: bool = False):
        """
        Returns a markdown link which can be used to link external websites, or
        even internal ones. If `link_url` is not provided, an empty link is
        returned.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_link('Visit this link')
            '[Visit this link]()'
            >>> m.new_link('Visit this link', 'http://shadyUrl.com/')
            '[Visit this link](http://shadyUrl.com/)'

        """
        link = MarkdownLinkGenerator()
        output = link.new_link(link_text, link_url, linebreak)
        return output

    def new_comment(self, comment_text: str):
        """ Returns the `comment_text` within markdown comment blocks.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_comment('This is a comment')
            '<!-- This is a comment -->'

        """
        comment_output = MarkdownTextGenerator()
        output = comment_output.new_comment(comment_text)
        return output

    def new_image(self, alt_text: str, image_url: str, image_title: str = ''):
        """
        Returns a markdown link which can be used to link external websites, or
        even internal ones. If `link_url` is not provided, an empty link is
        returned.

        .. code-block:: python

            >>> m = MarkdownGenerator()
            >>> m.new_image('image one', 'http://example.org/?image=one')
            '![image one](http://example.org/?image=one)'
            >>> m.new_image('image two', 'http://example.org/?image=second',
            ...   'The 2nd image')
            '![image two](http://example.org/?image=second "The 2nd image")'

        """
        image = MarkdownImageGenerator()
        output = image.new_image(alt_text, image_url, image_title)
        return output
