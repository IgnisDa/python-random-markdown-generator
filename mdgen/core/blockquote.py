class MarkdownBlockQuoteGenerator:
    
    """This class converts an input string into a markdown
    blockquote by adding '>' in the beginning
    of the string"""
    
    def new_blockquote(self, quote: str):
        """This is the method used to achieve what this class tends to"""
        quote = "> " + quote
        return quote
