import requests
import collections
import yaml


class Arguments:

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
    def parameters(elements: requests.models.Response) -> (str, dict, collections.namedtuple):
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

        # Hence, add the URL strings to the data parameters collection
        DataParameters = collections.namedtuple(typename='DataParameters', field_names=['data_url', 'schema_url'])
        return DataParameters._make((text['dataURL'], text['schemaURL']))
