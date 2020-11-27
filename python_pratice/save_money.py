# 定义原有存款
# 定义发工资模块
# 定义工资查询模块
# 启动方法
# 1定义原有存款
save_money = 1000
# 2定义发工资模块
import Money

# 3定义工资查询模块
def send_money():
    if Money.save_money == 2000:
        print('发工资啦')
    else:
        print("不开心，未收到工资")
# 4启动方法
if __name__ == '__main__':
    send_money()
    # slect_money()
