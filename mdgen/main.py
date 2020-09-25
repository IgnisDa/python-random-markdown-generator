from mdgen.markdown import MarkdownGenerator


class MarkdownOutputGenerator:

    def __init__(self):
        self.markdowngen = MarkdownGenerator()
        self.final_output = ''

    def add_text(self, text: str = None):
        self.final_output += self.markdowngen.new_text(text)

    def add_text_line(self, text: str = None):
        self.final_output += self.markdowngen.new_text_line(text)

    def add_header(self, text: str = None, header_level: int = None,
                   linebreak=True, atx=True):
        self.final_output += self.markdowngen.new_header(
            text, header_level, linebreak, atx
        )

    def add_bold_text(self, text: str = None):
        self.final_output += self.markdowngen.new_bold_text(text)

    def add_italic_text(self, text: str = None, underscore=False):
        self.final_output += self.markdowngen.new_italic_text(text, underscore)

    def add_bold_and_italic_text(self, text: str = None, underscore=False):
        self.final_output += self.markdowngen.new_bold_and_italic_text(text, underscore)

    def add_horizontal_rule(self, style: str = None):
        self.final_output += self.markdowngen.new_horizontal_rule(style)

    def add_paragraph(self, text: str = None, paragraph_size: int = 79):
        self.final_output += self.markdowngen.new_paragraph(text, paragraph_size)

    def get_output_text(self):
        return self.final_output
