import pytest
from mdgen.constants import LINESEPARATOR


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

    @pytest.mark.parametrize(
        'sample_data_size, paragraph_size',
        (
            (10, 5),
            (100, 100),
            (500, 23),
        )
    )
    def test_new_paragraph(self, sample_data_size,
                           paragraph_size, markdown_generator, faker):
        paragraph = faker.sentence(sample_data_size)
        markdowngen = markdown_generator()
        output = markdowngen.new_paragraph(paragraph, paragraph_size)
        assert output[-1] == LINESEPARATOR

    @pytest.mark.parametrize(
        'text, style, expected_output',
        (
            ('this is a test list one', 'asterisk', '* this is a test list one'),
            ('this is a test list two', 'plus', '+ this is a test list two'),
            ('this is a test list three', 'minus', '- this is a test list three'),
        )
    )
    def test_new_unordered_list_item(self, text, style, expected_output,
                                     markdown_generator):
        markdowngen = markdown_generator()
        output = markdowngen.new_unordered_list_item(text, style)
        assert output == expected_output

    @pytest.mark.parametrize(
        'text, index, expected_output',
        (
            ('this is a test list one', 1, '1. this is a test list one'),
            ('list item two', 2, '2. list item two'),
            ('part of ordered lists', 34, '34. part of ordered lists'),
        )
    )
    def test_new_ordered_list_item(self, text, index, expected_output,
                                   markdown_generator):
        markdowngen = markdown_generator()
        output = markdowngen.new_ordered_list_item(text, index)
        assert output == expected_output

    @pytest.mark.parametrize(
        'list_items_list, style, linebreak, expected_output',
        (
            (['one', 'two', 'three'], 'asterisk', True, '* one\n* two\n* three\n'),
            (['one', 'two', 'three'], 'asterisk', False, '* one\n* two\n* three'),
            (['hello', 'hi', 'hey'], 'plus', True, '+ hello\n+ hi\n+ hey\n'),
            (['hello', 'hi', 'hey'], 'plus', False, '+ hello\n+ hi\n+ hey'),
            (['day', 'night', 'evening'], 'minus', True, '- day\n- night\n- evening\n'),
            (['day', 'night', 'evening'], 'minus', False, '- day\n- night\n- evening'),
        )
    )
    def test_new_unordered_list(self, list_items_list, style, linebreak,
                                expected_output, markdown_generator):
        markdowngen = markdown_generator()
        output = markdowngen.new_unordered_list(list_items_list, style, linebreak)
        assert output == expected_output

    @pytest.mark.parametrize(
        'list_items_list, linebreak, expected_output',
        (
            (['one', 'two', 'three'],  True, '1. one\n2. two\n3. three\n'),
            (['one', 'two', 'three'],  False, '1. one\n2. two\n3. three'),
        )
    )
    def test_new_ordered_list(self, list_items_list, linebreak,
                              expected_output, markdown_generator):
        markdowngen = markdown_generator()
        output = markdowngen.new_ordered_list(list_items_list, linebreak)
        assert output == expected_output


class TestMarkdownGeneratorExceptions:

    @pytest.mark.parametrize(
        'input_data, header_level, linebreak, atx, expected_exception',
        (
            ('hello-header', 'str', True, True, AttributeError),
            ('hello-header', 1, object, True, AttributeError),
            ('hello-header', 1, False, object, AttributeError),
        )
    )
    def test_new_header(self, markdown_generator, input_data, header_level,
                        atx, linebreak, expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_header(
                input_data, header_level, linebreak, atx
            )

    @pytest.mark.parametrize(
        'input_data, underscore, expected_exception',
        (
            ('hello', object, '*hello*'),
        )
    )
    def test_new_italic_text(self, markdown_generator, input_data, underscore,
                             expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(AttributeError):
            markdowngen.new_italic_text(input_data, underscore)

    @pytest.mark.parametrize(
        'input_data, underscore, expected_exception',
        (
            ('hello', object, AttributeError),
        )
    )
    def test_new_bold_and_italic_text(self, markdown_generator, input_data, underscore,
                                      expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_bold_and_italic_text(input_data, underscore)

    @pytest.mark.parametrize(
        'style, expected_exception',
        (
            ('wrong-hyphens', AttributeError),
            ('wrong-asterisks', AttributeError),
            ('wrong-underscores', AttributeError),
        )
    )
    def test_new_horizontal_rule(self, markdown_generator, style,
                                 expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_horizontal_rule(style)

    @pytest.mark.parametrize(
        'text, style, expected_exception',
        (
            ('this is test one', 'wrong-plus', AttributeError),
            ('this is test two', 'wrong-asterisk', AttributeError),
            ('this is test three', 'wrong-minus', AttributeError),
        )
    )
    def test_new_unordered_list_item(self, markdown_generator, text, style,
                                     expected_exception):
        markdowngen = markdown_generator()
        with pytest.raises(expected_exception):
            markdowngen.new_unordered_list_item(text, style)
