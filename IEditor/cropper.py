import os
import shutil
import zipfile
from .cropperException import *


class Cropper:
    """A class that crop images in directory level and export  it to whatever output """

    Valid_Ext = ('png','jpeg','jpg','all')
    Non_Supported = ('gif','bitmap')
    ouptut_format = ('zip','directory')

    def __init__(self, directory='', width='', height='', top_level=True, format_type='all', path='.', output='all'):
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
        self.output = "OUTPUT.zip"
        self.width = width
        self.height = height
        self.path = path
        self.pic_out_format = Cropper.validator(Cropper.Valid_Ext, output)
        self.directory = self._directory(directory)
        self.top_level = top_level
        self.folder = True
        self.temp_directory = './temp_'

    def run_process(self):
        """ An object Manager """
        self.fetch_images()
        self.edit_images()
        self.export_images()

    def fetch_images(self):

        try:
            self._temp_dir('create')
            counter = 0
            if self.folder:
                folder = ''
                read_only = ''

                if self.top_level:
                    folder = os.listdir(self.directory)

                if not self.top_level:
                    folder = os.walk(self.directory)

                for file in folder:

                    if self.ext == 'all':
                        read_only = file.rsplit('.')[-1]

                    if file.endswith(self.ext) or read_only in Cropper.Valid_Ext:
                        shutil.copy(self._full_path(self.directory, file), self.temp_directory)
                        print(f"{file} copied successfully")
                        counter += 1

                print(f"Done, {counter} image(s) copied successfully")
                return True

        except Exception as e:
            print(f"Error Found: {e}")
            return False

    def export_images(self):
        """ export edited images in temporary directory to zip format  """
        try:
            if not os.listdir(self.temp_directory):
                raise EmptyDirectory("Empty folder")

            export = zipfile.ZipFile(self.output, 'w', compression=zipfile.ZIP_DEFLATED)

            for filename in os.listdir(self.temp_directory):
                export.write(self._full_path(self.temp_directory, filename), filename)

            shutil.rmtree(self.temp_directory)

        except EmptyDirectory as e:

            print(f"Error Found: {e}")

    def edit_images(self):
        pass

    def _directory(self, node):
        """ a checker that return either directory or file as output """
        try:
            if not os.path.isdir(f"{self.path}/{node}"):
                self.folder = False

                if not os.path.isfile(f"{self.path}/{node}"):
                    raise ParameterError("directory (required either file or directory) ")

            return f"{self.path}/{node}"

        except ParameterError as e:
            print(e)

        except IOError as e:
            print(e)
        return False

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
            shutil.rmtree(self.temp_directory)
            print(" Folder already exist \n deleting... \n  recreating temp folder")
            os.mkdir(self.temp_directory)

        except Exception as e:

            print(e)

        return False

    def _full_path(self, directory, relative_path):
        return os.path.join(directory, relative_path)

    @staticmethod
    def validator(lists, element):
        """ a method for validating list, tuple or dictionary """
        try:

            if element not in lists:
                raise IndexError(" Item not present ")

            return element

        except Exception as e:
            print("")