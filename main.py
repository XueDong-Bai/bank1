'''
人
类名：Person
属性：姓名 身份证号 电话号 卡
行为：开户、查询、取款、存款、转账、改密码、锁定、解锁、补卡、销户

卡
类名：Card
属性：卡号、密码、状态、余额


银行
类名：bank
属性：用户列表 提款机



提款机
类名：ATM
属性：
行为：开户、查询、取款、存款、转账、改密码、锁定、解锁、补卡、销户、退出


界面
类名：View
属性：
行为：管理员界面 管理员登录 系统功能界面
'''

from face import Face
import time
from atm import ATM


def m() :

    #界面对象
    vb = Face()
    #管理员开机界面
    vb.printAdminView()
    if  vb.userOperate("login"):
        return -1

    #获取ATM对象
    atm = ATM()


    while True :
        vb.printSysFunctionView()
        #等待用户的操作
        operate = input("请输入您的操作：")
        if operate == "1" :
            #开户
           atm.createUser();
        elif operate == "2" :
            print('查询')
        elif operate == "3" :
            print('取款')
        elif operate == "4":
            print('存款')
        elif operate == "5":
            print('转账')
        elif operate == "6":
            print('改密码')
        elif operate == "7":
            print('锁定')
        elif operate == "8":
            print('解锁')
        elif operate == "9":
            print('补卡')
        elif operate == "0":
            print('销户')
        elif operate == "t":
            if vb.userOperate("quit"):
                return -1

    time.sleep(1)


if __name__ == '__main__' :
    m()