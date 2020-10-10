import os

import pytest


class TestMarkdownOutputGenerator:

    @pytest.mark.parametrize(
        'input_dict, expected_output',
        (
            (
                [
                    dict(method='add_text', args=dict(text='hello')),
                    dict(method='add_text_line', args=dict(text='hello2')),
                ],
                'hellohello2\n'
            ),
            (
                [
                    dict(method='add_text', args=dict(text='hello')),
                    dict(method='add_linebreak', args=dict()),
                    dict(method='add_text_line', args=dict(text='hello2')),
                ],
                'hello\nhello2\n'
            ),
            (
                [
                    dict(
                        method='add_header',
                        args=dict(text='hello-header', header_level=1,
                                  linebreak=False, atx=False)
                    ),
                    dict(
                        method='add_header',
                        args=dict(text='hello-header', header_level=1)
                    )
                ],
                'hello-header\n------------\n# hello-header\n'
            ),
            (
                [
                    dict(
                        method='add_header',
                        args=dict(text='hello-header', header_level=1)
                    ),
                    dict(method='add_bold_text', args=dict(text='bold text')),
                ],
                '# hello-header\n**bold text**'
            ),
            (
                [
                    dict(method='add_italic_text',
                         args=dict(text='italic text', underscore=True)),
                    dict(method='add_bold_text', args=dict(text='bold text')),
                    dict(method='add_italic_text', args=dict(text='italic text two')),
                ],
                '_italic text_**bold text***italic text two*'
            ),
            (
                [
                    dict(method='add_bold_and_italic_text', args=dict(text='bold-italic')),
                    dict(method='add_bold_and_italic_text',
                         args=dict(text='bold-italic two', underscore=True)),
                ],
                '***bold-italic***_**bold-italic two**_'
            ),
            (
                [
                    dict(method='add_horizontal_rule', args=dict(style='hyphens')),
                    dict(method='add_horizontal_rule', args=dict(style='asterisks')),
                    dict(method='add_horizontal_rule', args=dict(style='underscores')),
                ],
                '---\n***\n___\n'
            ),
            (
                [
                    dict(method='add_paragraph',
                         args=dict(text='This is a test paragraph', paragraph_size=5)),
                    dict(method='add_horizontal_rule', args=dict(style='underscores')),
                ],
                'This is \na test \nparagraph \n___\n'
            ),
            (
                [
                    dict(method='add_unordered_list_item',
                         args=dict(text='This is a test list item', indent=1)),
                    dict(method='add_horizontal_rule', args=dict(style='underscores')),
                    dict(method='add_unordered_list_item',
                         args=dict(text='List item 2', indent=2, style='minus')),
                    dict(method='add_unordered_list_item',
                         args=dict(text='List item 3', style='plus')),
                ],
                '\t* This is a test list item\n___\n\t\t- List item 2\n+ List item 3\n'
            ),
            (
                [
                    dict(method='add_ordered_list_item',
                         args=dict(text='Test item', index=4, indent=2)),
                    dict(method='add_horizontal_rule', args=dict(style='underscores')),
                    dict(method='add_ordered_list_item',
                         args=dict(text='Hello test string', indent=3))
                ],
                '\t\t4. Test item\n___\n\t\t\t1. Hello test string\n'
            ),
            (
                [
                    dict(method='add_unordered_list',
                         args=dict(list_items_list=['one', 'two', 'three'])),
                    dict(method='add_unordered_list',
                         args=dict(list_items_list=[('one', 2), ('two', 1), 'three'])),
                    dict(method='add_horizontal_rule', args=dict(style='hyphens')),
                ],
                '* one\n* two\n* three\n\t\t* one\n\t* two\n* three\n---\n'
            ),
            (
                [
                    dict(method='add_ordered_list',
                         args=dict(list_items_list=['one', 'two', 'three'])),
                    dict(method='add_ordered_list',
                         args=dict(list_items_list=[('one', 2), ('two', 1), 'three'])),
                    dict(method='add_horizontal_rule', args=dict(style='hyphens')),
                    dict(method='add_ordered_list',
                         args=dict(list_items_list=[('one', 2, 3), ('two', 1), 'hah'])),
                ],
                (
                    '1. one\n1. two\n1. three\n\t\t1. one\n\t1. two\n1. three\n---\n'
                    '\t\t3. one\n\t1. two\n1. hah\n'
                )
            ),
            (
                [
                    dict(method='add_table',
                         args=dict(list_items_list=[
                             ['hello', 'hi', 'how do you do?'], ['1', '2', '3', '4']
                         ])),
                    dict(method='add_horizontal_rule', args=dict(style='hyphens')),
                ],
                '|hello|hi|how do you do?|\n|-----|--|--------------|\n|1|2|3|4|\n\n---\n'
            ),
            (
                [
                    dict(method='add_link',
                         args=dict(
                             link_text='Visit this link', linebreak=True,
                             link_url='http://shadyUrl.com/')
                         ),
                    dict(method='add_horizontal_rule', args=dict(style='hyphens')),
                    dict(method='add_link',
                         args=dict(
                             link_text='Visit', link_url='visit.com')
                         ),
                ],
                '[Visit this link](http://shadyUrl.com/)\n---\n[Visit](visit.com)\n'
            ),
            (
                [
                    dict(method='add_comment',
                         args=dict(comment_text='This is a comment text')),
                    dict(
                        method='add_code_block',
                        args=dict(code='import os\nprint("ok")', language='python')
                    ),
                ],
                '<!-- This is a comment text -->\n```python\nimport os\nprint("ok")\n```\n'
            ),
            (
                [
                    dict(method='add_blockquote',
                         args=dict(quote='Hahaha python goes brr')),
                    dict(method='add_comment',
                         args=dict(comment_text='This is a comment text')),
                ],
                '> Hahaha python goes brr\n<!-- This is a comment text -->\n'
            ),
            (
                [
                    dict(method='add_image',
                         args=dict(
                             alt_text='alt text', image_url='http://image-url.com/?img=1/',
                             image_title='This is the image title'
                         )),
                    dict(
                        method='add_code_block',
                        args=dict(code='import os\nprint("ok")', language='python')
                    ),
                ],
                (
                    '![alt text](http://image-url.com/?img=1/ "This is the image title")\n'
                    '```python\nimport os\nprint("ok")\n```\n'
                )
            ),
            (
                [
                    dict(
                        method='add_code_block',
                        args=dict(code='import os\nprint(os.uname())', language='python')
                    ),
                    dict(
                        method='add_code_block',
                        args=dict(code='for x in range(5):\n\tprint(x)', language='python')
                    ),
                ],
                (
                    '```python\nimport os\nprint(os.uname())\n```\n'
                    '```python\nfor x in range(5):\n\tprint(x)\n```\n'
                )
            )
        )
    )
    @ pytest.mark.testing
    def test_output_generator(self, input_dict, expected_output,
                              markdown_output_generator):
        markdownoutputgen = markdown_output_generator()
        for data in input_dict:
            func = getattr(markdownoutputgen, data['method'])
            func(**data['args'])
        output = markdownoutputgen.get_output_text()
        assert output == expected_output

    def test_output_file_created(self, markdown_output_generator):
        markdownoutputgen = markdown_output_generator()
        markdownoutputgen.add_comment('This is a comment')
        expected_output = '<!-- This is a comment -->\n'
        output = markdownoutputgen.get_output_text()
        assert output == expected_output
        markdownoutputgen.create_file_from_output('file.md')
        assert os.path.exists(markdownoutputgen.md_file)
        os.remove(markdownoutputgen.md_file)
