"""比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2、将数据配置到yaml文件里"""
import yaml


# 父类
class Animal:
    # 属性
    name = "动物"
    color = "彩色"
    age = 2
    gender = "male"

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 方法

    def yell(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


class Cat(Animal):
    fur = "毛发"

    def __init__(self, fur, name, color, age, gender):
        self.fur = fur
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name}技能是抓老鼠")

    def yell(self):
        print(f"{self.name}的叫声是喵喵喵")


class Dog(Animal):
    fur = "毛发"

    def __init__(self, fur, name, color, age, gender):
        self.fur = fur
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name}的技能是看家")

    def yell(self):
        print(f"{self.name}的叫声是汪汪汪")


if __name__ == '__main__':
    with open("animal.yml", encoding="UTF-8") as f:
        dates = yaml.safe_load(f)
        print(dates['Cat'])
        print(dates['Dog'])

xh = Cat("短毛", "小黑", "黑色", 2, "female")
xb = Dog("长毛", "小白", "白色", "3", "male")

print(f"{xh.name}的毛发是{xh.fur},{xh.name}的毛色是{xh.color},{xh.name}的年龄是{xh.age},{xh.name}的性别是{xh.gender}")
xh.yell()
xh.skill()

print(f"{xb.name}的毛发是{xb.fur},{xb.name}的毛色是{xb.color},{xb.name}的年龄是{xb.age},{xb.name}的性别是{xb.gender}")
xb.yell()
xb.skill()
