"""file system.

Implements a class that writes and reads n-files in a location in the files
system. Each file will be of type json.

"""
import json
import os
from typing import Dict, Optional


class FileSystem:
    """FileSystem.

    Implements the methods to write, read and create directories to store
    information in the file system. Each file created will be of type json.

    Attributes
    ----------
    path: str
        Location where the files will be stored.

    """

    __slots__ = ("path",)

    def __init__(self, path: str):
        """Constructor.

        Parameters
        ----------
        path: str
            Location where the files will be stored.

        """
        self.path = path

    def __create_dirs(self, nested_dirs: str) -> str:
        """Create Directory.

        Creates a nested directories inside the given path attribute.

        Parameters
        ----------
        nested_dirs: str
            Path to the nested directory. Beware of not use forward slashes at
            the start and the end of the string.

        Returns
        -------
        str
            Path of the new route to store the files.

        """
        path: str = f"{self.path}{nested_dirs}"
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def write(
        self, data: Dict, file_name: str, nested_dirs: Optional[str] = None
    ):
        """Write.

        Creates a new file in the location given by path attribute, in case
        that the user wants this file in a nested directory, this method calls
        __create_dirs to carry out this task.

        Parameters
        ----------
        data: Dict
            Data to store.
        file_name: str
            Name of the file to be created.
        nested_dirs: str
            Path to the nested directory. Beware of not use forward slashes at
            the start and the end of the string.

        """
        path: str = self.path
        if nested_dirs is not None:
            path = self.__create_dirs(nested_dirs=nested_dirs)
        with open(f"{path}/{file_name}.json", "w") as f:
            json.dump(data, f)

    def read(self, file_name: str, nested_dirs: Optional[str] = None) -> Dict:
        """Read.

        Loads a json file from the location given in the path attribute and the
        nested_dirs parameters.

        Parameters
        ----------
        file_name: str
            Name of the file to be created.
        nested_dirs: str
            Path to the nested directory. Beware of not use forward slashes at
            the start and the end of the string.

        """
        path: str = self.path
        if nested_dirs is not None:
            path = f"{path}/{nested_dirs}"
        with open(f"{path}/{file_name}.json") as f:
            data: Dict = json.load(f)
        return data
