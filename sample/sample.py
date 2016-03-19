#!/usr/bin/python
# -*- encoding: utf-8 -*-
from meta_parser.meta_parser import MetaParser


def main():
    schema = [
        {'input': 'og:title', 'output': 'title'},
        {'input': 'og:description', 'output': 'description'},
        {'input': 'og:image', 'output': 'image'},
        {'input': 'og:url', 'output': 'url'}
    ]

    urls = ['http://www.gazeta.ru/army/photo/kak_rossiya_voevala_v_sirii.shtml',
            'http://www.gazeta.ru/sport/2016/03/14/a_8123591.shtml']
    data = []

    for url in urls:
        result = MetaParser(url, schema).result
        data.append(result)
    print(data)


if __name__ == '__main__':
    main()
