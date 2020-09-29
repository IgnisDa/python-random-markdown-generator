from mdgen.constants import LINESEPARATOR, MARKDOWN_HEADER, MARKDOWN_HEADER_ALT


class MarkdownHeaderGenerator:
    """ This class creates markdown headers using input `text` and `level`. """

    def __init__(self, atx=True):
        self.atx = atx

    def new_header(self, text: str = None, header_level: int = None,
                   linebreak=True):
        if not self.atx:
            if linebreak:
                return (
                    f"{text}{LINESEPARATOR}"
                    f"{MARKDOWN_HEADER_ALT*len(text)}{LINESEPARATOR}"
                )
            else:
                return f"{text}{LINESEPARATOR}{MARKDOWN_HEADER_ALT*len(text)}"
        else:
            if linebreak:
                return (
                    f"{MARKDOWN_HEADER*(header_level)} {text}{LINESEPARATOR}"
                )
            else:
                return f"{MARKDOWN_HEADER*(header_level)} {text}"
