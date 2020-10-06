import inspect
import random

from faker import Faker

from mdgen.main import MarkdownOutputGenerator

_fake = Faker()


class DataProvider:

    def __init__(self):
        self.markdown_gen = MarkdownOutputGenerator()

    def random_blockquote(self):
        self.markdown_gen.add_blockquote(quote=_fake.sentence())

    def random_bold_and_italic_text(self):
        self.markdown_gen.add_bold_and_italic_text(
            text=_fake.sentence(),
            underscore=_fake.boolean()
        )

    def random_bold_text(self):
        self.markdown_gen.add_bold_text(_fake.word())

    def random_code_block(self):
        self.markdown_gen.add_code_block(
            code=_fake.paragraph(), language=_fake.word()
        )

    # def random_comment(self):
    #     output
    #

    # def random_header(self):
    #     output
    #

    # def random_horizontal_rule(self):
    #     output
    #

    # def random_image(self):
    #     output
    #

    # def random_italic_text(self):
    #     output
    #

    # def random_link(self):
    #     output
    #

    # def random_ordered_list(self):
    #     output
    #

    # def random_ordered_list_item(self):
    #     output
    #

    # def random_paragraph(self):
    #     output
    #

    # def random_table(self):
    #     output
    #

    # def random_text(self):
    #     output
    #

    # def random_text_line(self):
    #     output
    #

    # def random_unordered_list(self):
    #     output
    #

    # def random_unordered_list_item(self):
    #     output
    #

    def generate(self):
        members = inspect.getmembers(DataProvider, predicate=inspect.isfunction)
        eligible = [method for member, method in members if member.startswith('random')]
        random.shuffle(eligible)
        return eligible


if __name__ == "__main__":
    m = DataProvider()
    x = m.generate()
    for i in x:
        i(m)
    print(m.markdown_gen.get_output_text())
