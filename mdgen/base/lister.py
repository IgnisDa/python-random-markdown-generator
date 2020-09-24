class MarkdownListGenerator:

    list_symbol = '*'

    def __init__(self, style: str = 'asterisk'):
        if style == 'plus':
            self.list_symbol = '+'
        elif style == 'minus':
            self.list_symbol = '-'
        elif style == 'asterisk':
            self.list_symbol = '*'

    def new_unordered_list(self, text: str = None):
        return f"{self.list_symbol} {text}"
