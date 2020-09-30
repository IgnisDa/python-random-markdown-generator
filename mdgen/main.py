from mdgen.constants import LINESEPARATOR
from mdgen.markdown import MarkdownGenerator


class MarkdownOutputGenerator:

    def __init__(self):
        self.markdowngen = MarkdownGenerator()
        self.final_output = ''

    def get_output_text(self):
        return self.final_output

    def add_text(self, text: str):
        self.final_output += self.markdowngen.new_text(text)

    def add_text_line(self, text: str):
        self.final_output += self.markdowngen.new_text_line(text)

    def add_header(self, text: str, header_level: int = None,
                   linebreak=True, atx=True):
        self.final_output += self.markdowngen.new_header(
            text, header_level, linebreak, atx
        )

    def add_bold_text(self, text: str):
        self.final_output += self.markdowngen.new_bold_text(text)

    def add_italic_text(self, text: str, underscore=False):
        self.final_output += self.markdowngen.new_italic_text(text, underscore)

    def add_bold_and_italic_text(self, text: str, underscore=False):
        self.final_output += self.markdowngen.new_bold_and_italic_text(text, underscore)

    def add_horizontal_rule(self, style: str):
        self.final_output += self.markdowngen.new_horizontal_rule(style)

    def add_paragraph(self, text: str, paragraph_size: int = 79):
        self.final_output += self.markdowngen.new_paragraph(text, paragraph_size)

    def add_unordered_list_item(self, text: str, style: str = 'asterisk'):
        self.final_output += self.markdowngen.new_unordered_list_item(text, style)
        self.final_output += LINESEPARATOR

    def add_ordered_list_item(self, text: str, index: int = 1):
        self.final_output += self.markdowngen.new_ordered_list_item(text, index)
        self.final_output += LINESEPARATOR

    def add_unordered_list(self, list_items_list: list, style: str = 'asterisk',
                           linebreak: bool = True):
        self.final_output += self.markdowngen.new_unordered_list_item(
            list_items_list, style, linebreak
        )
        self.final_output += LINESEPARATOR

    def add_ordered_list(self, list_items_list: list, linebreak: bool = True):
        self.final_output += self.markdowngen.new_ordered_list(
            list_items_list, linebreak
        )
        self.final_output += LINESEPARATOR

    def add_table(self, list_items_list: list):
        self.final_output += self.markdowngen.new_table(list_items_list)
        self.final_output += LINESEPARATOR

    def add_link(self, link_text: str, link_url: str = '', linebreak: bool = False):
        self.final_output += self.markdowngen.new_link(link_text, link_url, linebreak)
        self.final_output += LINESEPARATOR

    def add_comment(self, comment_text: str):
        self.final_output += self.markdowngen.new_comment(comment_text)
        self.final_output += LINESEPARATOR

    def add_image(self, alt_text: str, image_url: str, image_title: str = ''):
        self.final_output += self.markdowngen.new_image(alt_text, image_url, image_title)
        self.final_output += LINESEPARATOR
