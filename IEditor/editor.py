from .cropper import Cropper
from PIL import Image
import os


class Editor(Cropper):
    """
    A class that inherit cropper to have all its functionality.
    it uses the 'is a' relationship

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def edit_images(self):

        counter = 1
        for image in os.listdir(self.temp_directory):

            ext = image.rsplit('.')[-1]
            name = f"{counter}.{ext}"
            resize = (self.width, self.height)
            try:
                node = Image.open(self._full_path(self.temp_directory,image))
                node.thumbnail(resize, Image.ANTIALIAS)
                node.save(self._full_path(self.temp_directory,name))
                print("image edited successfully")
                os.unlink(self._full_path(self.temp_directory,image))

            except IOError:

                print(f"unable to read image {image}")

            counter +=1










