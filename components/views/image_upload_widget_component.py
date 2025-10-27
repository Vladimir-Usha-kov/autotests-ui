from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.input import Input
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.empty_view_component = EmptyViewComponent(page, identifier)
        self.preview_image = Image(page,f'{identifier}-image-upload-widget-preview-image', 'Image')

        self.image_upload_icon = Icon(page,f'{identifier}-image-upload-widget-info-icon', 'Icon')
        self.image_upload_title = Text(page,f'{identifier}-image-upload-widget-info-title-text', 'Title')
        self.image_upload_description = Text(page,
            f'{identifier}-image-upload-widget-info-description-text', 'Description')

        self.button_upload = Button(page,f'{identifier}-image-upload-widget-upload-button', 'Upload image')
        self.button_remove = Button(page,f'{identifier}-image-upload-widget-remove-button',
                                    'Remove image')
        self.upload_input = FileInput(page,f'{identifier}-image-upload-widget-input', 'Input upload')


    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        self.image_upload_icon.check_visible()

        self.image_upload_title.check_visible()
        self.image_upload_title.check_have_text('Tap on "Upload image" button to select file')

        self.image_upload_description.check_visible()
        self.image_upload_description.check_have_text('Recommended file size 540X300')

        self.button_upload.check_visible()

        if is_image_uploaded:
            self.button_remove.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            self.empty_view_component.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.button_remove.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_file(file)