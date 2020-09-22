from mdgen.base.header import MarkdownHeaderGenerator
from mdgen.base.text import MarkdownTextGenerator


class MarkdownGenerator:

    def new_text(self, text: str = None):
        output = MarkdownTextGenerator(text)
        return output.new_text()

    def new_header(self, text: str = None, header_level: int = None,
                   linebreak=True):
        output = MarkdownHeaderGenerator(text, header_level, linebreak)
        return output.new_header()
