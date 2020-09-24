from mdgen.base import (MarkdownBoldGenerator, MarkdownHeaderGenerator,
                        MarkdownHorizontalRuleGenerator,
                        MarkdownItalicGenerator, MarkdownListGenerator,
                        MarkdownTextGenerator)


class MarkdownGenerator:

    def new_text(self, text: str = None):
        text_output = MarkdownTextGenerator()
        output = text_output.new_text(text)
        return output

    def new_text_line(self, text: str = None):
        text_line = MarkdownTextGenerator()
        output = text_line.new_text_line(text)
        return output

    def new_header(self, text: str = None, header_level: int = None,
                   linebreak=True, atx=True):
        if not isinstance(header_level, (int,)):
            raise AttributeError(f"`header_level` must be an instance of or {int}")
        if not isinstance(linebreak, (bool,)):
            raise AttributeError(f"`linebreak` must be an instance of or {bool}")
        if not isinstance(atx, (bool,)):
            raise AttributeError(f"`atx` must be an instance of or {bool}")
        header = MarkdownHeaderGenerator(atx)
        output = header.new_header(text, header_level, linebreak)
        return output

    def new_bold_text(self, text: str = None):
        bold_text = MarkdownBoldGenerator()
        output = bold_text.new_bold_text(text)
        return output

    def new_italic_text(self, text: str = None, underscore=False):
        if not isinstance(underscore, (bool,)):
            raise AttributeError(f"`underscore` must be an instance of or {bool}")
        italic_text = MarkdownItalicGenerator()
        output = italic_text.new_italic_text(text, underscore)
        return output

    def new_bold_and_italic_text(self, text: str = None, underscore=False):
        if not isinstance(underscore, (bool,)):
            raise AttributeError(f"`underscore` must be an instance of or {bool}")
        bolded = self.new_bold_text(text)
        bolded_and_italic = self.new_italic_text(bolded, underscore)
        return bolded_and_italic

    def new_horizontal_rule(self, style: str = None):
        permitted_styles = ['hyphens', 'asterisks', 'underscores']
        if style not in permitted_styles:
            raise AttributeError(f"`style` must be among {permitted_styles}")
        horizontal_rule = MarkdownHorizontalRuleGenerator()
        output = horizontal_rule.new_horizontal_rule(style)
        return output

    def new_paragraph(self, text: str = None, paragraph_size: int = 79):
        paragraph = MarkdownTextGenerator(paragraph_size)
        output = paragraph.new_paragraph(text)
        return output

    def new_unordered_list(self, text: str = None, style: str = 'asterisk'):
        permitted_styles = ['asterisk', 'plus', 'minus']
        if style not in permitted_styles:
            raise AttributeError(f"`style` must be among {permitted_styles}")
        list_item = MarkdownListGenerator(style)
        output = list_item.new_unordered_list(text)
        return output
