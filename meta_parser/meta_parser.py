import requests
from bs4 import BeautifulSoup


class MetaParser(object):
    def __init__(self, parsed_url, output_schema):
        self._url = parsed_url
        self._result = BeautifulSoup(requests.get(parsed_url).text, 'lxml')
        self._schema = output_schema

    # noinspection PyShadowingBuiltins
    @property
    def result(self):
        data = {}

        for input, output in self._schema.items():
            results = self._result.findAll(attrs={'property': input})

            if len(results) == 0:
                raise RuntimeError('Page {url} has not meta tag with {input} property'.format(
                    url=self._url, input=input))

            value = results[0]['content']

            if value:
                data[output] = value.strip()

        return data
