from config.conf import REPORT_FILE
import pytest



if __name__ == '__main__':
    # pytest.main(["-m smoke", f"--html={REPORT_FILE}"])
    # pytest.main(['--alluredir=reports/allure_data', "-m", "success"])
    pytest.main([f'--alluredir={REPORT_FILE}'])
    # run pytest
    # pytest -sv demo --alluredir = reports/allure_data
    # allure report
    # allure generate reports/allure_data -o allure_report --clean