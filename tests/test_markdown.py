import pytest


class TestMarkdownGenerator:

    @pytest.mark.parametrize(
        'input_data, expected_output',
        (
            ('hello', 'hello'),
            ('markdown_text', 'markdown_text')
        )
    )
    def test_new_text(self, markdown_generator, input_data, expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_text(input_data)
        assert output == expected_output

    @pytest.mark.parametrize(
        'input_data, header_level, linebreak, expected_output',
        (
            ('hello', 4, True, '#### hello\n'),
            ('hello', 4, False, '#### hello'),
            ('markdown_text', 1, True, '# markdown_text\n'),
            ('markdown_text', 1, False, '# markdown_text'),
        )
    )
    def test_new_header(self, markdown_generator, input_data, header_level,
                        linebreak, expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_header(input_data, header_level, linebreak)
        assert output == expected_output
