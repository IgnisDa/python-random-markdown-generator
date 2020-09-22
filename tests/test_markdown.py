import pytest


class TestMarkdownGenerator:

    @pytest.mark.parametrize(
        'input_data, expected_output',
        (
            ('hello', 'hello'),
            ('markdown-text', 'markdown-text')
        )
    )
    @pytest.mark.testing
    def test_new_text(self, markdown_generator, input_data, expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_text(input_data)
        print(output)
        assert output == expected_output

    @pytest.mark.parametrize(
        'input_data, expected_output',
        (
            ('hello', 'hello\n'),
            ('markdown_text', 'markdown_text\n')
        )
    )
    def test_new_text_line(self, markdown_generator, input_data,
                           expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_text_line(input_data)
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

    @pytest.mark.parametrize(
        'input_data, expected_output',
        (
            ('hello',  '**hello**'),
            ('this stuff is awesome ', '**this stuff is awesome**'),
            ('markdown_text\n',  '**markdown_text**'),
        )
    )
    def test_new_bold_text(self, markdown_generator, input_data,
                           expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_bold_text(input_data)
        assert output == expected_output

    @pytest.mark.parametrize(
        'input_data, underscore, expected_output',
        (
            ('hello', False, '*hello*'),
            ('this stuff is awesome ', False, '*this stuff is awesome*'),
            ('markdown-text\n', False, '*markdown-text*'),
            ('hello', True, '_hello_'),
            ('this stuff is awesome ', True, '_this stuff is awesome_'),
            ('markdown-text\n', True, '_markdown-text_'),
        )
    )
    def test_new_italic_text(self, markdown_generator, input_data, underscore,
                             expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_italic_text(input_data, underscore)
        assert output == expected_output

    @pytest.mark.parametrize(
        'input_data, underscore, expected_output',
        (
            ('hello', False, '***hello***'),
            ('this stuff is awesome ', False, '***this stuff is awesome***'),
            ('markdown_text\n', False, '***markdown_text***'),
            ('hello', True, '_**hello**_'),
            ('this stuff is awesome ', True, '_**this stuff is awesome**_'),
            ('markdown_text\n',  True, '_**markdown_text**_'),
        )
    )
    def test_new_bold_and_italic_text(self, markdown_generator, input_data,
                                      underscore, expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_bold_and_italic_text(input_data, underscore)
        assert output == expected_output

    @pytest.mark.parametrize(
        'style, expected_output',
        (
            ('hyphens', '---'),
            ('asterisks', '***'),
            ('underscores', '___'),
        )
    )
    def test_new_horizontal_rule(self, markdown_generator, style,
                                 expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_horizontal_rule(style)
        assert output == expected_output
