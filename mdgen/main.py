from mdgen.constants import LINESEPARATOR
from mdgen.markdown import MarkdownGenerator


class MarkdownOutputGenerator(MarkdownGenerator):

    def __init__(self, filepath='output.md'):
        self.final_output = ''
        self.md_file = filepath

    def add_linebreak(self):
        self.final_output += self.new_linebreak()

    def get_output_text(self):
        return self.final_output

    def add_text(self, text: str):
        self.final_output += self.new_text(text)

    def add_text_line(self, text: str):
        self.final_output += self.new_text_line(text)

    def add_header(self, text: str, header_level: int = None,
                   linebreak=True, atx=True):
        self.final_output += self.new_header(
            text, header_level, linebreak, atx
        )
        if not linebreak:
            self.final_output += LINESEPARATOR

    def add_bold_text(self, text: str):
        self.final_output += self.new_bold_text(text)

    def add_italic_text(self, text: str, underscore=False):
        self.final_output += self.new_italic_text(text, underscore)

    def add_bold_and_italic_text(self, text: str, underscore=False):
        self.final_output += self.new_bold_and_italic_text(text, underscore)

    def add_horizontal_rule(self, style: str):
        self.final_output += self.new_horizontal_rule(style)

    def add_paragraph(self, text: str, paragraph_size: int = 79):
        self.final_output += self.new_paragraph(text, paragraph_size)

    def add_unordered_list_item(self, text: str, indent: int = 0, style: str = 'asterisk'):
        self.final_output += self.new_unordered_list_item(text, indent, style)
        self.final_output += LINESEPARATOR

    def add_ordered_list_item(self, text: str, indent: int = 0, index: int = 1):
        self.final_output += self.new_ordered_list_item(text, indent, index)
        self.final_output += LINESEPARATOR

    def add_unordered_list(self, list_items_list: list, style: str = 'asterisk',
                           linebreak: bool = True):
        self.final_output += self.new_unordered_list(
            list_items_list, style, linebreak
        )

    def add_ordered_list(self, list_items_list: list, linebreak: bool = True):
        self.final_output += self.new_ordered_list(
            list_items_list, linebreak
        )

    def add_table(self, list_items_list: list):
        self.final_output += self.new_table(list_items_list)
        self.final_output += LINESEPARATOR

    def add_link(self, link_text: str, link_url: str = '', linebreak: bool = False):
        # :code:`linebreak` is ignored since if it passes as `True`, two LINESEPARATOR
        # would be added
        self.final_output += self.new_link(link_text, link_url, False)
        self.final_output += LINESEPARATOR

    def add_comment(self, comment_text: str):
        self.final_output += self.new_comment(comment_text)
        self.final_output += LINESEPARATOR

    def add_image(self, alt_text: str, image_url: str, image_title: str = ''):
        self.final_output += self.new_image(alt_text, image_url, image_title)
        self.final_output += LINESEPARATOR

    def add_code_block(self, code: str, language: str = 'python'):
        self.final_output += self.new_code_block(code, language)
        self.final_output += LINESEPARATOR

    def add_blockquote(self, quote: str):
        self.final_output += self.new_blockquote(quote)
        self.final_output += LINESEPARATOR

    def create_file_from_output(self, filepath='output.md'):
        self.md_file = filepath
        with open(self.md_file, 'w') as md_file:
            md_file.write(self.get_output_text())
