from mdgen.constants import LINESEPARATOR, MARKDOWN_HEADER


class MarkdownHeaderGenerator:
    """ This class creates markdown headers using input `text` and `level`. """

    def new_header(self, text: str = None, header_level: int = None,
                   linebreak=True):
        if not linebreak:
            return f"{MARKDOWN_HEADER*(header_level)} {text}"
        return f"{MARKDOWN_HEADER*(header_level)} {text}{LINESEPARATOR}"
