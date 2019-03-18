import os
import shutil
from .cropperException import *


class Cropper:
    """A class that crop images in directory level and export  it to whatever output """

    Valid_Ext = ('png','jpeg','jpg','all')
    Non_Supported = ('gif','bitmap')
    ouptut_format = ('zip','directory')

    def __init__(self, directory='', width='', height='', top_level=True, format_type='all', path='.'):
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
        self.path = path
        self.pic_out_format = Cropper.validator(Cropper.Valid_Ext, format_type)
        self.directory = self._directory(directory)
        self.top_level = top_level
        self.folder = True
        self.temp_directory = f'{self.path}/temp_'

    def run_process(self):
        """ An object Manager """
        self.fetch_images()
        self.edit_images()
        self.export_images()

    def fetch_images(self):

        try:
            self._temp_dir('create')

            if self.folder:
                folder = ''

                if self.top_level:
                    folder = os.listdir(self.directory)

                if not self.top_level:
                    pass

                for file in folder:

                    if self.Ext == 'all':
                        read_only = file.rsplit('.')[-1]

                    if file.endswith(self.Ext) or read_only in Cropper.Valid_Ext:
                        shutil.copy(file, self.temp_directory)

        except :
            pass

        finally:
            pass


    def export_images(self):
        pass

    def edit_images(self):
        pass

    def _directory(self, directory):
        """ a checker that return either directory or file as output """
        try:
            if not os.path.isdir(f"{self.path}/{directory}"):
                self.folder = False

                if not os.path.isfile(f"{self.path}/{directory}"):
                    raise ParameterError("directory (required either file or directory) ")

            return f"{self.path}/{directory}"

        except ParameterError as e:
            print(e)

        return False


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

    def _temp_dir(self, action='create'):
        """
        Perform simple function with this method
        it help create or delete temporary folder

        """
        try:
            if action == 'create':

                os.mkdir(self.temp_directory)

            if action == 'delete':

                shutil.rmtree(self.temp_directory)

            return True

        except FileExistsError:

            print("Folder already exist")
        except Exception as e:

            print(e)

        return False
