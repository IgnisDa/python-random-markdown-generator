import inspect
import random

from faker import Faker

from mdgen.main import MarkdownOutputGenerator

_fake = Faker()


def create_list_items_list_for_table():
    return (_fake.sentences(3) for _ in range(5))


def create_list_items_list_for_list():
    return _fake.sentences()


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

    def random_comment(self):
        self.markdown_gen.add_comment(comment_text=_fake.sentence())

    def random_header(self):
        self.markdown_gen.add_header(
            text=_fake.sentence(), header_level=random.randint(1, 6),
            atx=_fake.boolean(), linebreak=_fake.boolean()
        )

    def random_horizontal_rule(self):
        permitted_styles = ['hyphens', 'asterisks', 'underscores']
        self.markdown_gen.add_horizontal_rule(style=random.choice(permitted_styles))

    def random_image(self):
        self.markdown_gen.add_image(
            alt_text=_fake.sentence(), image_url=_fake.url(), image_title=_fake.text()
        )

    def random_italic_text(self):
        self.markdown_gen.add_italic_text(
            text=_fake.sentence(), underscore=_fake.boolean()
        )

    def random_link(self):
        self.markdown_gen.add_link(
            link_text=_fake.sentence(), link_url=_fake.url(), linebreak=_fake.boolean()
        )

    def random_ordered_list(self):
        self.markdown_gen.add_ordered_list(
            list_items_list=create_list_items_list_for_list(), linebreak=_fake.boolean()
        )

    def random_ordered_list_item(self):
        self.markdown_gen.add_ordered_list_item(
            text=_fake.sentence(), indent=_fake.boolean(), index=random.randint(1, 10)
        )

    def random_paragraph(self):
        self.markdown_gen.add_paragraph(
            text=_fake.paragraph(), paragraph_size=random.randint(60, 100)
        )

    def random_table(self):
        self.markdown_gen.add_table(list_items_list=create_list_items_list_for_table())

    def random_text(self):
        self.markdown_gen.add_text(text=_fake.word())

    def random_text_line(self):
        self.markdown_gen.add_text_line(text=_fake.sentence())

    def random_unordered_list(self):
        self.markdown_gen.add_ordered_list(
            list_items_list=create_list_items_list_for_list(), linebreak=_fake.boolean()
        )

    def random_unordered_list_item(self):
        permitted_styles = ['asterisk', 'plus', 'minus']
        self.markdown_gen.add_unordered_list_item(
            text=_fake.sentence(), indent=random.randint(1, 4),
            style=random.choice(permitted_styles)
        )

    def get_output_text(self):
        return self.markdown_gen.get_output_text()

    def insert_lineseparator_to_output(self):
        self.markdown_gen.add_linebreak()


def generate():
    members = inspect.getmembers(DataProvider, predicate=inspect.isfunction)
    eligible = [member for member, method in members if member.startswith('random')]
    eligible = random.choice(eligible)
    return eligible
