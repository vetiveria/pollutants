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

        DataParameters = collections.namedtuple(typename='DataParameters', field_names=['data_url', 'schema_url'])
        return DataParameters._make((text['dataURL'], text['schemaURL']))
