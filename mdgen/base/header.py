from mdgen.constants import LINESEPARATOR, MARKDOWN_HEADER


class MarkdownHeaderGenerator:
    """ This class creates markdown headers using input `text` and `level`. """

    def __init__(self, text: str = None, header_level: int = None,
                 linebreak=True):
        self.text = text
        self.header_level = header_level
        self.linebreak = linebreak

    def new_header(self):
        if not self.linebreak:
            return f"{MARKDOWN_HEADER*(self.header_level)} {self.text}"
        return (
            f"{MARKDOWN_HEADER*(self.header_level)} {self.text}{LINESEPARATOR}"
        )
