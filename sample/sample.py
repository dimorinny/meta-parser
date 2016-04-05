#!/usr/bin/python
# -*- encoding: utf-8 -*-
from meta_parser import MetaParser


def main():
    schema = {
        'og:title': 'title',
        'og:description': 'description',
        'og:image': 'image',
        'relap-image': 'url'
    }

    urls = ['https://news.mail.ru/incident/25361692/',
            'http://www.novayagazeta.ru/society/72528.html']
    data = []

    for url in urls:
        result = MetaParser(url, schema).result
        data.append(result)
    print(data)


if __name__ == '__main__':
    main()
