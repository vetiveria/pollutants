"""Module directories"""
import os


class Directories:
    """
    Class Directories
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def cleanup(directories_: list):
        """
        Clean-up

        :param directories_: A list of directories
        :return:
        """

        for path in directories_:

            if not os.path.exists(path):
                continue

            [os.remove(os.path.join(base, file))
             for base, directories, files in os.walk(path)
             for file in files]

            [os.removedirs(os.path.join(base, directory))
             for base, directories, files in os.walk(path, topdown=False)
             for directory in directories
             if os.path.exists(os.path.join(base, directory))]

    @staticmethod
    def create(directories_: list):
        """
        Create

        :param directories_: A list of directories
        :return:
        """

        for path in directories_:
            if not os.path.exists(path):
                os.makedirs(path)
