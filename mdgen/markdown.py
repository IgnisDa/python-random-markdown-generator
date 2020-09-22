from mdgen.base import (MarkdownBoldGenerator, MarkdownHeaderGenerator,
                        MarkdownHorizontalRuleGenerator,
                        MarkdownItalicGenerator, MarkdownTextGenerator)


class MarkdownGenerator:

    def new_text(self, text: str = None):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        text_output = MarkdownTextGenerator()
        output = text_output.new_text(text)
        return output

    def new_text_line(self, text: str = None):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        text_line = MarkdownTextGenerator()
        output = text_line.new_text_line(text)
        return output

    def new_header(self, text: str = None, header_level: int = None,
                   linebreak=True, atx=True):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        if not isinstance(header_level, (int,)):
            raise ValueError(f"`header_level` must be an instance of or {int}")
        if not isinstance(linebreak, (bool,)):
            raise ValueError(f"`linebreak` must be an instance of or {bool}")
        if not isinstance(atx, (bool,)):
            raise ValueError(f"`atx` must be an instance of or {bool}")
        header = MarkdownHeaderGenerator()
        output = header.new_header(text, header_level, linebreak, atx)
        return output

    def new_bold_text(self, text: str = None):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        bold_text = MarkdownBoldGenerator()
        output = bold_text.new_bold_text(text)
        return output

    def new_italic_text(self, text: str = None, underscore=False):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        italic_text = MarkdownItalicGenerator()
        output = italic_text.new_italic_text(text, underscore)
        return output

    def new_bold_and_italic_text(self, text: str = None, underscore=False):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        bolded = self.new_bold_text(text)
        bolded_and_italic = self.new_italic_text(bolded, underscore)
        return bolded_and_italic

    def new_horizontal_rule(self, style: str = None):
        permitted_styles = ['hyphens', 'asterisks', 'underscores']
        if not isinstance(style, (str, int)):
            raise ValueError(f"`style` must be an instance of {str}")
        if style not in permitted_styles:
            raise ValueError(f"`style` must be among {permitted_styles}")
        horizontal_rule = MarkdownHorizontalRuleGenerator()
        output = horizontal_rule.new_horizontal_rule(style)
        return output
