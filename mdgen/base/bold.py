from mdgen.constants import MARKDOWN_BOLD


class MarkdownBoldGenerator:
    """ This class creates markdown bold text using input `text`."""

    def new_bold_text(self, text: str = None):
        return f"{MARKDOWN_BOLD}{text.strip()}{MARKDOWN_BOLD}"
