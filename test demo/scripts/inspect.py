#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import cm
from utils.time import running_time


@running_time
def inspect_element():
    """
    simple inspection of yaml file format
    """
    for files in os.listdir(cm.DATA_PATH):
        _path = os.path.join(cm.DATA_PATH, files)
        with open(_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        for k in data.values():
            try:
                pattern, value = k.split(':')
            except ValueError:
                raise Exception("Element expression have no `:`")
            if pattern not in cm.LOCATE_MODE:
                raise Exception('Element %s in %s have not type' % (k, _path))
            elif pattern == 'xpath':
                assert '//' in value,\
                    'Element %s in %s xpath type, value not matching' % (k, _path)
            elif pattern == 'css':
                assert '//' not in value, \
                    'Element %s in %s css type, value not matching' % (k, _path)
            else:
                assert value, 'Element %s in %s type, value not matching' % (k, _path)


if __name__ == '__main__':
    inspect_element()