from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.empty_view_component = EmptyViewComponent(page, identifier)

        self.preview_image = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')

        self.image_upload_icon = page.get_by_test_id(f'{identifier}-image-upload-widget-info-icon')
        self.image_upload_title = page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        self.image_upload_description = page.get_by_test_id(
            f'{identifier}-image-upload-widget-info-description-text')
        self.button_upload = page.get_by_test_id(f'{identifier}-image-upload-widget-upload-button')
        self.button_remove = page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')
        self.upload_input = page.get_by_test_id(f'{identifier}-image-upload-widget-input')


    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        expect(self.image_upload_icon).to_be_visible()

        expect(self.image_upload_title).to_be_visible()
        expect(self.image_upload_title).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.image_upload_description).to_be_visible()
        expect(self.image_upload_description).to_have_text('Recommended file size 540X300')

        expect(self.button_upload).to_be_visible()

        if is_image_uploaded:
            expect(self.button_remove).to_be_visible()
            expect(self.preview_image).to_be_visible()

        if not is_image_uploaded:
            self.empty_view_component.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.button_remove.click()


    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)