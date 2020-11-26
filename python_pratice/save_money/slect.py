# 3定义工资查询模块
import money


def slect_money():
    current_money = money.save_money
    if current_money == 2000:
        print('发工资啦')
    else:
        print("不开心，未收到工资")


if __name__ == '__main__':
