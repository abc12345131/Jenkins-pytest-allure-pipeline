import pytest
import yaml
from elements.excel_data import ExcelData
from utils.api import ApiMethods

class TestLogin:
    
    #parse yaml file
    with open("api.yaml", "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    #parse xlsx file
    data = ExcelData("api")



    apiTrain= ApiMethods(data)

    @pytest.mark.parametrize(('data_dict', 'path_dict', 'assert_dict'), data.list_data, ids=data.list_desc)
    def test_1(self, data_dict, path_dict, assert_dict):

        res = self.apiTrain.get(url)
        data = res.get('data')
        assert data is not None