import json
import os
import pprint
import sys
from os.path import isfile, isdir

log_list = []


def parse_log(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            d = dict()
            d['%h'] = line.split(' ')[0]
            d['%t'] = line.split(' ')[3].lstrip('[') + line.split(' ')[4].rstrip(']')
            d['%r'] = (line.split(' ')[5].lstrip('\"'), line.split(' ')[6], line.split(' ')[7].rstrip('\"'))
            d['%s'] = line.split(' ')[8]
            d['%b'] = line.split(' ')[9]
            d['%{Referer}'] = line.split(' ')[10].lstrip('\"').rstrip('\"')
            d['%{User-Agent}'] = line.split(' ')[11:-1]
            d['%D, ms'] = line.split(' ')[-1].rstrip('\n')
            log_list.append(d)
    return log_list


def log_file_reader():
    my_list = []
    if len(sys.argv) == 1:
        filename = '/Users/sergejdmitriev/Desktop/Logs/access_50.log'
    else:
        filename = sys.argv[1]
    if isfile(filename):
        my_list = parse_log(filename)
    elif isdir(filename):
        for file in os.listdir(filename):
            print(file)
            if file != '.DS_Store':
                my_list = parse_log(filename + file)

    return my_list


log_list = log_file_reader()


def requests_count():
    return len(log_list)


def count_by_methods():
    dict_methods = {}
    for line in log_list:
        if line.get('%r')[0] in dict_methods:
            dict_methods[line.get('%r')[0]] += 1
        else:
            dict_methods[line.get('%r')[0]] = 1
    return dict_methods


def count_by_ip():
    dict_ips = {}
    for line in log_list:
        if line.get('%h') in dict_ips:
            dict_ips[line.get('%h')] += 1
        else:
            dict_ips[line.get('%h')] = 1
    sorted_dict = sorted(dict_ips.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict[:3]


def slow_requests():
    sorted_dict = sorted(log_list, key=lambda d: d['%D, ms'], reverse=True)
    return sorted_dict[:3]


def statistic_to_json():
    statistic_json = {'request_count': requests_count(), 'http_methods_count': count_by_methods(),
                      'top_ip': count_by_ip(), 'top_long': slow_requests()}

    with open('analyze.json', 'w') as f:
        json.dump(statistic_json, f, indent=4)

    with open('analyze.json') as json_file:
        data = json.load(json_file)
        pprint.pprint(data)


statistic_to_json()
