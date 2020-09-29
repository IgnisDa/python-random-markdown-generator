from mdgen.constants import MARKDOWN_ITALIC, MARKDOWN_ITALIC_ALT


class MarkdownItalicGenerator:
    """ This class creates markdown bold text using input `text`."""

    def new_italic_text(self, text: str = None, underscore=False):
        if not underscore:
            return f"{MARKDOWN_ITALIC}{text.strip()}{MARKDOWN_ITALIC}"
        return f"{MARKDOWN_ITALIC_ALT}{text.strip()}{MARKDOWN_ITALIC_ALT}"
