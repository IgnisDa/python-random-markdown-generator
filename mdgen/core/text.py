from mdgen.constants import (LINESEPARATOR, MARKDOWN_COMMENT_CLOSE,
                             MARKDOWN_COMMENT_OPEN)


class MarkdownTextGenerator:
    """ This class creates markdown text using input `text`. """

    def __init__(self, paragraph_size=79):
        self.paragraph_size = paragraph_size

    def new_text(self, text: str = None):
        return f"{text}"

    def new_text_line(self, text: str = None):
        return f"{text}\n"

    def new_paragraph(self, text: str = None):
        text_list = text.split()
        output = []
        word_counter = 0
        for word in text_list:
            output.append(word)
            word_counter += len(word)
            if word_counter >= self.paragraph_size:
                word_counter = 0
                output.append(LINESEPARATOR)
        output = ' '.join(output)
        output = output.replace(f"{LINESEPARATOR} ", LINESEPARATOR)
        if output[-1] != LINESEPARATOR:
            output = f"{output}{LINESEPARATOR}"
        return output

    def new_comment(self, comment_text: str):
        return f"{MARKDOWN_COMMENT_OPEN} {comment_text} {MARKDOWN_COMMENT_CLOSE}"
