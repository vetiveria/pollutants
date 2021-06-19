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

            files_ = [os.remove(os.path.join(base, file))
                      for base, directories, files in os.walk(path) for file in files]
            if any(files_):
                raise Exception('Unable to delete all files within path {}'.format(path))

            paths_ = [os.removedirs(os.path.join(base, directory))
                            for base, directories, files in os.walk(path, topdown=False)
                            for directory in directories if os.path.exists(os.path.join(base, directory))]
            if any(paths_):
                raise Exception('Unable to delete all directories within path {}'.format(path))

            if os.path.exists(path):
                os.rmdir(path)


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
