import pytest

import toxicants.io.arguments


class TestArguments:

    @pytest.fixture()
    def urlstring(self):
        return 'https://raw.githubusercontent.com/miscellane/hub/develop/data/countries/us/environment/toxins/chemicals/chemicalsEnvirofacts.yaml'

    def test_url(self, urlstring):

        arguments = toxicants.io.arguments.Arguments()

        req = arguments.url(urlstring=urlstring)
        assert req.status_code == 200, "The string is  a valid URL string"





