import numpy as np
import requests
import json

import pandas as pd


class ReadSchema:

    def __init__(self):
        """
        Constructor
        """

        self.__dictionary = {'integer': int, 'string': str, 'double': float}

    @staticmethod
    def __content(schema_url: str) -> dict:
        """
        Loads the contents of a schema file
        :param schema_url:
        :return:
        """

        try:
            req = requests.get(url=schema_url)
            req.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise err

        return json.loads(req.content)

    def __types(self, series: pd.Series) -> pd.Series:
        """
        Maps the Apache Spark data type in the schema file to the corresponding Python data type, as outlined in
        self.dictionary http://spark.apache.org/docs/2.4.8/sql-reference.html
        :param series: A pandas Series
        :return:
        """

        return series.apply(lambda x: self.__dictionary[x])

    @staticmethod
    def __attributes(blob: pd.DataFrame) -> (np.ndarray, dict):
        """

        :param blob:
        :return:
        """

        usecols = blob.name.values
        dtype = blob[['name', 'localtype']].set_index(keys='name', drop=False, inplace=False).\
            to_dict(orient='dict')['localtype']

        return usecols, dtype

    def exc(self, schema_url: str) -> (np.ndarray, dict):
        """
        Execute
        :param schema_url:
        :return:
        """

        # Get the contents of the schema file
        content = self.__content(schema_url=schema_url)

        # Extract the 'fields' object.  The data schema is defined within this object
        fields = pd.DataFrame.from_dict(data=content['fields'], orient='columns')

        # Map each field's in-schema data type to the corresponding Python data type
        fields.loc[:, 'localtype'] = self.__types(fields['type'])

        return self.__attributes(blob=fields[['name', 'localtype']])
