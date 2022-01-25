#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import cm

class Element(object):
    """locate page element"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(cm.DATA_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s file does not exist" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """get attribute"""
        data = self.data.get(item)
        if data:
            name, value = data.split(':')
            return name, value
        raise ArithmeticError("Cannot find {} in {}".format(item, self.file_name))


if __name__ == '__main__':
    element = Element('webpage')
    print(element['search'])