from user import  User
from card import  Card
import random
class ATM(object) :
    def __init__(self):
        # 存储所有用户的信息
        self.users = {}
    #开户
    def createUser(self):
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")

        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0 :
            print("预存款输入有误！开户失败。。。")
            return -1
        onePassword = input("请设置密码：")
        if  not self.checkPasswd(onePassword) :
            print("两次密码不一致！开户失败")
            return False

        #所有需要的信息全了
        cardId = self.randomCardID()
        card = Card(cardId ,onePassword ,prestoreMoney)
        user = User(name,idCard,phone,card)

        #存到字典
        self.users[cardId] = user
        print("开户成功，请牢记卡号 %s"  % cardId)
    #查询
    def searchUser(self):
        pass
    #取款
    def withdrawals(self):
        pass
    #存款
    def saveMoney(self):
        pass
    #转账
    def transferMoney(self):
        pass
    #改密码
    def changePass(self):
        pass
    #锁定
    def lockUser(self):
        pass
    #解锁
    def unLockUser(self):
        pass
    #补卡
    def reNewCard(self):
        pass
    #销户
    def killUser(self):
        pass

    # 验证密码
    def checkPasswd(self , realPasswd):
        for i in range(3) :
            tempPasswd = input("请再次输入密码：")
            if tempPasswd == realPasswd :
                return True
        return False

    #生成卡号
    def randomCardID(self):
        while True :
            str = ""
            for i in range(6) :
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str +=  ch
            #判断是否重复
            if not self.users.get(str) :
                return str
