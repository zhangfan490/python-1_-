# 定义原有存款
# 定义发工资模块
# 定义工资查询模块
# 启动方法
# 1定义原有存款
save_money = 1000
# 2定义发工资模块
import money


def send_money():
    money.save_money = 2000
    print('发工资啦')


# 3定义工资查询模块
import money


def slect_money():
    current_money = money.save_money
    if current_money == 2000:
        print('发工资啦')
    else:
        print("不开心，未收到工资")


if _name_ == '_main_':

# 4启动方法


from send_money import send_money
from slect_money import slect_money

if _name_ == '_main_':
    send_money()
    slect_money()
