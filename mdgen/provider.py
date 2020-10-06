from faker.providers import BaseProvider

# from mdgen.generator import DataProvider
from mdgen.main import MarkdownOutputGenerator


class MarkdownPostProvider(BaseProvider):

    output_generator = MarkdownOutputGenerator()

    def post(self, size: str = 'small'):
        allowed_sizes = {'small': 10, 'medium': 20, 'large': 50}
        try:
            num_methods_to_add = allowed_sizes[size]
        except KeyError:
            raise ValueError(f"`{size = }` not among {list(allowed_sizes.keys())}")
        for num in range(num_methods_to_add):
            print('ok')
        return self.output_generator.get_output_text()
