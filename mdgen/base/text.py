class MarkdownTextGenerator:
    """ This class creates markdown text using input `text`. """

    def __init__(self, text: str = None):
        self.text = text

    def new_text(self):
        return f"{self.text}"
