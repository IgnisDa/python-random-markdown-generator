from faker.providers import BaseProvider

from mdgen.generator import DataProvider, generate


class MarkdownPostProvider(BaseProvider):

    def post(self, size: str = 'small'):
        allowed_sizes = {'small': 10, 'medium': 20, 'large': 50}
        try:
            num_methods_to_add = allowed_sizes[size]
        except KeyError:
            raise ValueError(f"`{size}` not among {list(allowed_sizes.keys())}")
        data_generator = DataProvider()
        for _ in range(num_methods_to_add):
            generated_method = generate()
            getattr(data_generator, generated_method)()
            data_generator.insert_lineseparator_to_output()

        return data_generator.get_output_text()
