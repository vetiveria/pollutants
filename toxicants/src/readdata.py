"""Module readdata"""
import collections

import pandas as pd


class ReadData:
    """
    Class ReadData
    """

    def __init__(self, specifications: collections.namedtuple):
        """
        Constructor

        :param specifications:
                    specifications.data_url -> The data URL |
                    specifications.usecols -> The data file fields to be read |
                    specifications.dtype -> A dictionary of the fields to be read and their data types |
                    specifications.rename -> Do one or more fields have to be renamed?  |
                    specifications.dictionary_of_names -> If 'rename' is True, a dictionary of the fields to be renamed and
                    their new names
        """

        self.specifications = specifications

    def __read(self) -> pd.DataFrame:
        """
        Reads the data
        :return:
        """

        try:
            data = pd.read_csv(filepath_or_buffer=self.specifications.data_url, header=0, usecols=self.specifications.usecols,
                               dtype=self.specifications.dtype, encoding='UTF-8')
        except FileNotFoundError as err:
            raise Exception(err.strerror)

        return data

    def __rename(self, blob: pd.DataFrame) -> pd.DataFrame:
        """
        Renames the fields of DataFrame blob
        :param blob:
        :return:
        """

        return blob.rename(columns=self.specifications.dictionary_of_names)

    def exc(self):
        """
        Entry point.
        :return:
        """

        # Read the data into a DataFrame
        data = self.__read()

        # If required, rename fields
        if self.specifications.rename:
            data = self.__rename(blob=data.copy())

        return data
