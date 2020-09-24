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
                    dict(method='add_bold_text', args=dict(text='bold text'))
                ],
                '**bold text**'
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
