from mdgen.constants import (LINESEPARATOR, MARKDOWN_HORIZONTAL_RULE_ASTERISKS,
                             MARKDOWN_HORIZONTAL_RULE_HYPHENS,
                             MARKDOWN_HORIZONTAL_RULE_UNDERSCORES)


class MarkdownHorizontalRuleGenerator:
    """ This class creates markdown headers using input `text` and `level`. """

    def new_horizontal_rule(self, style: str = None):
        if style == 'hyphens':
            return f"{MARKDOWN_HORIZONTAL_RULE_HYPHENS}{LINESEPARATOR}"
        elif style == 'asterisks':
            return f"{MARKDOWN_HORIZONTAL_RULE_ASTERISKS}{LINESEPARATOR}"
        if style == 'underscores':
            return f"{MARKDOWN_HORIZONTAL_RULE_UNDERSCORES}{LINESEPARATOR}"
