"""
Module instances:
    Validates key contents of the toxic chemicals data set
"""
import pandas as pd


class Instances:
    """
    Class Instances
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def __validate(blob: pd.DataFrame) -> pd.DataFrame:
        """
        This function validates the contents of the tri_chem_id field.  In brief: each
            CAS Code must be 10 characters long, and the first chracter must be a number
            TRI Code must be 4 characters long, and the first character must be 'N'

        :param blob:
        :return:
        """

        cas = blob['tri_chem_id'].apply(lambda x: len(x) == 10) & blob['tri_chem_id'].apply(lambda x: x[0].isnumeric())
        tri = blob['tri_chem_id'].apply(lambda x: len(x) == 4) & blob['tri_chem_id'].apply(lambda x: x[0] == 'N')

        return blob.loc[(cas | tri), :]

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        # Delete instances that do not have a chemical identification code
        blob = data.copy().loc[~data['tri_chem_id'].isna(), :]

        # If the name of the chemical is missing -> empty string instead of NaN
        blob['chem_name'].fillna(value='', inplace=True)

        # Retrieve the instances that have a valid chemical identification code
        blob = self.__validate(blob=blob.copy())

        return blob
