import random
import os
import time,datetime
from core import logger
from core import accounts
from core import db_handler
from conf import setting

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')


def add_account():
    acc_dict = {}
    flag = True
    while flag:
        print('欢迎进入新用户注册界面'.center(50, '-'))
        acc_dict['name'] = input('请输入持卡人姓名: ')
        acc_dict['password'] = input('请输入密码: ')
        acc_dict['id'] = random.randint(1,6),
        acc_dict['enroll_date'] = time.asctime()
        two_year_datetime = datetime.datetime.now() + datetime.timedelta(days = 730)
        acc_dict['expire_date'] = time.ctime(time.mktime(two_year_datetime.timetuple()))
        acc_dict['status'] = 0

        db_path = db_handler.db_handler(setting.DATABASE)

        if os.path.exists('%s.json' % os.path.join(db_path,acc_dict['id'])):
            print('用户名重复，请重新注册')
            continue
        else:
            accounts.dump_account(acc_dict)
            print('您注册的用户信息如下'.center(50, '-'))
            print('''
            持卡人姓名：    %s
            卡号：          %d
            注册时间：      %s
            过期时间：      %s
            用户状态：      %d
            ''') %(acc_dict['name'],acc_dict['id'],acc_dict['enroll_date'],acc_dict['expire_date'],acc_dict['status'])
    return


def locked_account():
    pass


def update_credit():
    pass


def quit_mg(acc_data):
    exit()


def  mg_interactive():
    print('欢迎进入ATM后台管理接口'.center(50, '-'))
    menu = '''
    \33[34;0m
    [1] 添加信用卡
    [2] 冻结/解冻信用卡
    [3] 提升信用卡额度
    [4] 退出
    \33[0m
    '''
    menu_dic = {
        '1': add_account,  # 后面的不能加‘’如 ‘account_info’
        '2': locked_account,
        '3': update_credit,
        'q': quit_mg,
    }
    exit_flag = True
    while exit_flag:
        print(menu)
        choice = input('>>: ').strip()
        if len(choice) == 0: continue
        if choice in menu_dic:
            menu_dic.get(choice)()
        else:
            print('\33[31;1mSelect is not exist !\033[0m')