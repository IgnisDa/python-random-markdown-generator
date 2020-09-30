import pytest


class TestMarkdownOutputGenerator:

    @pytest.mark.parametrize(
        'input_dict, expected_output',
        ()
    )
    def test_output_generator(self, input_dict, expected_output,
                              markdown_output_generator):
        markdownoutputgen = markdown_output_generator()
        for data in input_dict:
            func = getattr(markdownoutputgen, data['method'])
            func(**data['args'])
        output = markdownoutputgen.get_output_text()
        print(repr(output), repr(expected_output))
        assert output == expected_output
