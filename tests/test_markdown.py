import pytest


class TestMarkdownGenerator:

    @pytest.mark.parametrize(
        'input_data, expected_output',
        (
            ('hello', 'hello'),
            ('markdown-text', 'markdown-text')
        )
    )
    def test_new_text(self, markdown_generator, input_data, expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_text(input_data)
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
        'input_data, header_level, linebreak, atx, expected_output',
        (
            ('hello', 4, True, True, '#### hello\n'),
            ('hello', 4, False, True, '#### hello'),
            ('markdown_text', 1, True, True, '# markdown_text\n'),
            ('markdown_text', 1, False, True, '# markdown_text'),
            ('hello', 4, True, False, 'hello\n-----\n'),
            ('hello', 4, False, False, 'hello\n-----'),
            ('markdown', 1, True, False, 'markdown\n--------\n'),
            ('markdown', 1, False, False, 'markdown\n--------'),
        )
    )
    def test_new_header(self, markdown_generator, input_data, header_level,
                        atx, linebreak, expected_output):
        markdowngen = markdown_generator()
        output = markdowngen.new_header(
            input_data, header_level, linebreak, atx
        )
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


class TestMarkdownGeneratorExceptions:

    @pytest.mark.parametrize(
        'input_data, expected_exception',
        (
            (None, ValueError),
            (object, ValueError)
        )
    )
    @pytest.mark.testing
    def test_new_text(self, markdown_generator, input_data,
                      expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_text(input_data)

    @pytest.mark.parametrize(
        'input_data, expected_exception',
        (
            (None, ValueError),
            (object, ValueError)
        )
    )
    @pytest.mark.testing
    def test_new_text_line(self, markdown_generator, input_data,
                           expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_text_line(input_data)

    @pytest.mark.parametrize(
        'input_data, header_level, linebreak, atx, expected_exception',
        (
            (None, 4, True, True, ValueError),
            ('hello-header', 'str', True, True, ValueError),
            ('hello-header', 1, object, True, ValueError),
            ('hello-header', 1, False, object, ValueError),
        )
    )
    def test_new_header(self, markdown_generator, input_data, header_level,
                        atx, linebreak, expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_header(
                input_data, header_level, linebreak, atx
            )

    @ pytest.mark.parametrize(
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

    @ pytest.mark.parametrize(
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
