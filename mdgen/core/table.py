from mdgen.constants import (LINESEPARATOR, MARKDOWN_TABLE_COL_SEPARATOR,
                             MARKDOWN_TABLE_ROW_SEPARATOR)


class MarkdownTableGenerator:
    """ This will create markdown tables using a list of lists. """

    def new_table(self, list_items_list: list):
        output = ''
        for index, list_item in enumerate(list_items_list):
            output += (
                f"{MARKDOWN_TABLE_COL_SEPARATOR}"
                f"{MARKDOWN_TABLE_COL_SEPARATOR.join(list_item)}"
                f"{MARKDOWN_TABLE_COL_SEPARATOR}{LINESEPARATOR}"
            )
            if index == 0:
                temp_cols = (f"{MARKDOWN_TABLE_ROW_SEPARATOR*len(p)}" for p in list_item)
                temp = f"{MARKDOWN_TABLE_COL_SEPARATOR.join(temp_cols)}"
                output += (
                    f"{MARKDOWN_TABLE_COL_SEPARATOR}{temp}{MARKDOWN_TABLE_COL_SEPARATOR}"
                    f"{LINESEPARATOR}"
                )
        return output
