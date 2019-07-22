import time
class Face(object) :
    admin = "1"
    password = "1"

    def printAdminView(self):
        print("******************************************************")
        print("*                                                    *")
        print("*                                                    *")
        print("*                  欢迎登录银行系统                  *")
        print("*                                                    *")
        print("*                                                    *")
        print("******************************************************")



    def printSysFunctionView(self):
        print("******************************************************")
        print("*      开户（1）              查询（2）              *")
        print("*      取款（3）              存款（4）              *")
        print("*      转账（5）              改密码（6）            *")
        print("*      锁定（7）              解锁（8）              *")
        print("*      补卡（9）              销户（0）              *")
        print("*                   退出（t）                        *")
        print("******************************************************")

    def userOperate(self , flag):
        # print('请输入管理员账号：')
        result = -1
        vResult = -1
        if flag =="login" :
            vResult = -1
        elif flag == "quit" :
            vResult = 0
        inputAdmin = input('请输入管理员账号：')
        if self.admin != inputAdmin:
            print('账号输入有误')
            return vResult
        inputPass = input('请输入管理员密码：')
        if self.password != inputPass:
            print('密码有误')
            return vResult
        # 能执行到这里说明账号密码正确
        if flag =="login" :
            print('登录成功！请稍后。。。')
            result = 0
        elif flag == "quit" :
            print('退出成功！请稍后。。。')
            result = -1
        time.sleep(2)
        return result

