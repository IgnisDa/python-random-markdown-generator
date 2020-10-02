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
                    dict(
                        method='add_header',
                        args=dict(text='hello-header', header_level=1,
                                  linebreak=True, atx=False)
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
            # (
            #     [
            #         dict(method='add_ordered_list_item',
            #              args=dict(text='Test item', index=4, indent=2)),
            #         dict(method='add_horizontal_rule', args=dict(style='underscores')),
            #         dict(method='add_ordered_list_item',
            #              args=dict(text='Hello test string', indent=3))
            #     ],
            #     '\t\t4. Test item\n___\n3. Hello test string\n'
            # ),
            (
                [
                    dict(
                        method='add_code_block',
                        args=dict(code='import os\nprint(os.cwd())', language='python')
                    ),
                    dict(
                        method='add_code_block',
                        args=dict(code='for x in range(5):\n\tprint(x)', language='python')
                    ),
                ],
                '```python\nimport os\nprint(os.cwd())\n```\n' +
                '```python\nfor x in range(5):\n\tprint(x)\n```\n'
            )
        )
    )
    def test_output_generator(self, input_dict, expected_output,
                              markdown_output_generator):
        markdownoutputgen = markdown_output_generator()
        for data in input_dict:
            func = getattr(markdownoutputgen, data['method'])
            func(**data['args'])
        output = markdownoutputgen.get_output_text()
        assert output == expected_output
