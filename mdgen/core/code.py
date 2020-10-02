from mdgen.constants import MARKDOWN_CODEBLOCK, LINESEPARATOR


class MarkdownCodeGenerator:
    """ This class creates markdown code using input `code`."""

    def new_code_block(self, code: str, language: str = 'python'):
        return (f"{MARKDOWN_CODEBLOCK}{language}{LINESEPARATOR}{code.strip()}"
                f"{LINESEPARATOR}{MARKDOWN_CODEBLOCK}")
