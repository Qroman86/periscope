#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib
import urllib2


def subway_model_parse(url):
    print('url is %s' % url)
    response = requests.get(url)
    print(response.content)


# define number of subway station
def count_number_of_subway_station(root_url):
    start_station_index = 1
    end_station_index = 20

    # payload = {'from': '1', 'to': '20', 'route': '0'}
    data = {}
    data['from'] = '1'
    data['to'] = '10'
    data['route'] = '0'
    url_values = urllib.urlencode(data)
    full_url = root_url + '?' + url_values
    response = urllib2.urlopen(full_url)
    html = response.read()
    print(html)
    # response = requests.get(root_url, params=payload)
    # print(response.url)

    content = html
    is_end_station_index_in_array_bounds = is_correct_stations_choose(content)
    print('is_out_of_bound: %s' % is_end_station_index_in_array_bounds)

    return 0


def prepare_full_url(root_url, start_index, end_station_index):
    return root_url + '?from=' + str(start_index) + '&to=' + str(end_station_index) + '&route=0'


def is_correct_stations_choose(current_content):
    start_stop_word = 'Выберите начальную'
    stop_stop_word = 'и конечную станции'
    print(current_content.rfind(start_stop_word))

    if current_content.rfind(start_stop_word) != -1:
        return False
    if current_content.rfind(stop_stop_word) != -1:
        return False
    return True


count_number_of_subway_station('http://metro.yandex.ru/minsk')
#


# subway_model_parse('http://ya.ru')
# сделать шаг назад и попробовать выгрузить данные по метро из java
# посмотреть
