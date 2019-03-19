import allure
import pytest


class TestAll():
    # 添加测试描述
    # @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step("测试新增信息")
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test01(self):
        allure.attach('点击新增按钮','娃哈哈')
        allure.attach('输入收货地址','嘤嘤嘤')
        prnt('01运行了')

    @allure.step('测试删除信息')
    def test02(self):
        allure.attach('开始删除','嗯嗯嗯')
        print('02运行了')

    # 标记优先级，方式一
    @allure.severity('critical')
    def test03(self):
        print('验证优先级')
    # 标记优先级，方式二
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test04(self):
        print('官网方式，麻烦')


