from exceptions import InvalidFolderName
from datastore.tables import get_folders_db


class Folder:

    def __init__(self, folder_name, folder_id=None, user_id=None ):
        self.folder_name = folder_name
        self.folder_id = folder_id
        self.user_id = user_id

    def dict_attributes(self):

        return {
            'folder_name': f"'{self.folder_name}'",
            'user_id': f'{self.user_id}'
        }

    @property
    def folder_name(self):
        return self._folder_name

    @folder_name.setter
    def folder_name(self, value):
        if not value in ['inbox' , 'draft' , 'sent']:
            raise InvalidFolderName
        self._folder_name= value


class FolderManager:
    folder = Folder
    folders_db = get_folders_db()

    @classmethod
    def make_folder(cls , folder_name , user_id):
        try:
            folder_instance = cls.folder(folder_name , user_id= user_id)
            folder_id = cls.folders_db.insert(folder_instance.dict_attributes())
            return folder_id
        except InvalidFolderName as err:
            print(err)
