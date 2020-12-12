import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    data = yaml.safe_load(f)
    add_datas = data['add']['datas']
    add_myid = data['add']['add_myid']
    div_datas = data['div']['datas']
    div_myid = data['div']['div_myid']


def test_a():
    print("测试用例_加法+除法")


# def func():
# print("普通函数")

class TestCalc:

    # 定义类级别 setup
    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    #定义类级别 teardown
    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=add_myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add 方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，做出保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后需要写断言
        assert result == expect

    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas, ids=div_myid
    )
    def test_div(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add 方法
        result = self.calc.div(a, b)
        # 判断result是浮点数，做出保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后需要写断言
        assert result == expect

    # def test_add2(self):
    # result = self.calc.add(0.1, 0.2)
    # assert round(result, 2) == 0.3

    # def test_add1(self):
    # 实例化计算器类
    # calc = Calculator()
    # 调用add 方法
    # result = self.calc.add(0.1, 0.1)
    # 得到结果后需要写断言
    # assert result == 0.2

    # def test_add2(self):
    # 实例化计算器类
    # calc = Calculator()
    # 调用add 方法
    # result = self.calc.add(-1, -1)
    # 得到结果后需要写断言
    # assert result == -2
