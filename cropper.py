import os
from .cropperException import *


class Cropper:
    """A class that crop images in directory level and export  it to whatever output """

    Valid_Ext = ('png','jpeg','jpg','all')
    Non_Supported = ('gif','bitmap')
    ouptut_format = ('zip','directory')

    def __init__(self, directory='', width='', height='', top_level='', format_type='all'):
        """
        Set all variable needed
        Parameter lists
        directory : specify the directory where images will be extracted from
        width :  specify the width of the new images
        height : specify the height of the new images
        top_level :  specify if it should perform deep level search of images in directory
        format_type : specify the format of images to search for
        pic_out_format : specify the format in which the images will be output for
        
        """
        self.ext = Cropper.validator(Cropper.Valid_Ext, format_type)
        self.output_directory = "OUTPUT"
        self.width = width
        self.height = height
        self.pic_out_format = Cropper.validator(Cropper.Valid_Ext, format_type)

    def run_process(self):
        """ An object Manager """
        self.fetch_images()
        self.edit_images()
        self.export_images()

    def fetch_images(self):
        pass


    def export_images(self):
        pass

    def edit_images(self):
        pass

    @staticmethod
    def validator(lists, element ):
        """ a method for validating list, tuple or dictionary """
        try:
            if not isinstance(lists, list):
                raise ParameterError('A list is required')

            if element not in lists:
                raise IndexError(" Item not present ")

            return element

        except ParameterError as e:
            pass

        except IndexError as e:
            pass

        except Exception as e:
            pass
