'''
dict 客户端
功能 : 发起请求,接收结果
'''

from socket import *
import sys
import getpass

ADDR = ('127.0.0.1',8888)
s = socket()
s.connect(ADDR)

#注册功能
def do_register():
    while True:
        name = input('User:')
        pwd = getpass.getpass('Password:')
        pwd1 = getpass.getpass('PasswordAgain:')
        if pwd != pwd1:
            print('两次密码不一致!')
            continue
        if (' ' in name) or (' ' in pwd):
            print('用户名或密码不能含有空格')
            continue
        msg = 'R %s %s' % (name,pwd)
        s.send(msg.encode())#发送请求
        data = s.recv(128).decode()#接收反馈
        if data == 'OK':
            print('注册成功')
        else:
            print('注册失败')
        return

#登录功能
def do_login():
    while True:
        name = input('User:')
        pwd = getpass.getpass('Password:')
        msg = 'L %s %s' % (name, pwd)
        s.send(msg.encode())  # 发送请求
        data = s.recv(128).decode()  # 接收反馈
        if data == 'OK':
            print('登录成功')
            login(name)
            break
        else:
            print('登录失败')

#查询单词
def do_query(name):
    while True:
        word = input('输入单词:')
        if word == '##':
            break
        msg = 'Q %s %s' % (name,word)
        s.send(msg.encode())  # 发送请求
        data = s.recv(2048).decode()  # 接收反馈
        print(data)

def do_histroy(name):
    msg = 'H %s' % (name)
    s.send(msg.encode())  # 发送请求
    while True: #不确定有多少历史记录
        data = s.recv(1024).decode()  # 接收反馈
        if data == '##':
            break
        print(data)

#登录后的二级界面
def login(name):
    while True:
        print('\n==========%s Query==========='% name)
        print('******     1.查单词    ******')
        print('******    2.历史记录   ******')
        print('******     3.注销      ******')
        print('===========================')
        cmd = input('选项(1,2,3):')
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_histroy(name)
        elif cmd == '3':
            return #二级界面结束
        else:
            print('输入有误,请输入正确命令')

#搭建网络
def main():
    while True:
        print('\n==========Welcome==========')
        print('******     1.注册     ******')
        print('******     2.登录     ******')
        print('******     3.退出     ******')
        print('===========================')
        cmd = input('选项(1,2,3):')
        s.send(cmd.encode())
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            s.close()
            sys.exit('谢谢使用')
        else:
            print('输入有误,请输入正确命令')


if __name__ == '__main__':
    main()



