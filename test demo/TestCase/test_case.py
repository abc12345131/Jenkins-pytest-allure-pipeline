import os
import pytest

import jsonpath

from elements.excel_data import ExcelData
from utils.allure_reports import allure_report_get
from utils.api import ApiTest

data = ExcelData('data')


class TestCase(object):
    @pytest.mark.parametrize(('data_dict', 'path_dict', 'assert_dict'), data.list_data, ids=data.list_desc)
    def test_1(self, data_dict, path_dict, assert_dict):
        response = ApiTest(path_dict)
        allure_report_get(response.header_print, response.url, response.response_json)
        assert response.status_code == assert_dict['status_code'], 'HTTP status code'
        for i in path_dict.keys():
            if '$' in i:
                res = jsonpath.jsonpath(response.json(), i)
                assert res == assert_dict['i']

    @pytest.mark.parametrize(('data_dict', 'path_dict', 'assert_dict'), [data.list_data[1]], ids=[data.list_desc[1]])
    def test_2(self, data_dict, path_dict, assert_dict):
        response = ApiTest(path_dict)
        assert response.status_code == assert_dict['status_code'], 'HTTP status code'
        for i in path_dict.keys():
            if '$' in i:
                res = jsonpath.jsonpath(response.json(), i)
                assert res == assert_dict['i']


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', 'reports\test_all'])
    os.system('allure serve reports\test_all')