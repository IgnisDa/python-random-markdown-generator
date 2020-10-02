class MarkdownImageGenerator:

    def new_image(self, alt_text: str, image_url: str, image_title: str = ''):
        output = f"![{alt_text}]({image_url} \"{image_title}\")"
        if not image_title:
            output = output.replace(' ""', '')
        return output
