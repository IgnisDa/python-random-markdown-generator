from mdgen.constants import LINESEPARATOR


class MarkdownLinkGenerator:

    def new_link(self, link_text: str, link_url: str, linebreak: bool = False):
        output = f"[{link_text}]({link_url})"
        if linebreak:
            output += LINESEPARATOR
        return output
