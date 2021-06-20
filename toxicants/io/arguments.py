"""
Module arguments:
    Parses the package's input argument, which is a YAML URL, and extracts the contents of the YAML
"""
import collections
import requests
import yaml


class Arguments:
    """
    Class Arguments
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def url(urlstring) -> requests.models.Response:
        """
        Ascertains that the URL argument is valid
        :param urlstring: A URL string (to a YAML file)
        :return:
        """

        try:
            req = requests.get(url=urlstring)
            req.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise err

        return req

    @staticmethod
    def parameters(elements: requests.models.Response) -> collections.namedtuple:
        """
        :param elements: The content of the input YAML file
        :return:
        """

        text = yaml.safe_load(elements.text)

        # Are the URL strings valid?
        data_url = text['dataURL']
        assert requests.head(url=data_url).status_code == 200, "The YAML dataURL string  is invalid"
        schema_url = text['schemaURL']
        assert requests.head(url=schema_url).status_code == 200, "The YAML schemaURL string  is invalid"

        # Field names
        rename = text['rename']
        assert isinstance(rename, bool), "The value of YAML parameter 'rename' must either be True or False"

        if rename:
            dictionary_of_names = text['dictionaryOfNames']
            assert isinstance(dictionary_of_names, dict), "A dictionary names, wherein the old name is the key and the new " \
                                                          "name is the value, is required for renaming data fields"
            assert len(dictionary_of_names) > 0, "The dictionary of names is empty"
        else:
            dictionary_of_names = {}

        # Hence, add the URL strings to the data parameters collection
        DataParameters = collections.namedtuple(typename='DataParameters',
                                                field_names=['data_url', 'schema_url', 'rename', 'dictionary_of_names'])
        return DataParameters._make((data_url, schema_url, rename, dictionary_of_names))
