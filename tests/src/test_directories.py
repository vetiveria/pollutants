import pytest
import os

import toxicants.src.directories


class TestDirectories:

    @pytest.fixture()
    def list_of_directories(self):
        return ['temporary']

    def test_create(self, list_of_directories):
        directories = toxicants.src.directories.Directories()
        directories.create(directories_=list_of_directories)

        for directory in list_of_directories:
            assert os.path.exists(directory), "The directory {} could not be created".format(directory)

    def test_cleanup(self, list_of_directories):
        directories = toxicants.src.directories.Directories()
        directories.cleanup(directories_=list_of_directories)

        for directory in list_of_directories:
            assert not os.path.exists(directory), "The directory {} was not deleted".format(directory)
