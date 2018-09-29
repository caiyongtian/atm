from core import auth
from core import logger
from core import accounts
from core import transaction

user_data = {
    'is_auth': False,
    'account_data': None,
    'account_id': None
}

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')


def account_info(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    print('Account Info'.center(50,'-'))
    print(u'''
    持卡人：  %s
    卡号：    %s
    余额：    %d
    额度：    %d
    还款日：  %d
    '''%(account_data['name'],account_data['id'],account_data['balance'],account_data['credit'],account_data['pay_date']))


def repay(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    print('Balance Info'.center(50, '-'))
    print(u'''
    余额：           %d
    本期应还金额：    %d
    还款日：         %d
    ''' %(account_data['balance'],account_data['credit'] - account_data['balance'],account_data['pay_date']))
    back_flag = True
    while back_flag:
        repay_amount = input('\33[33;1mInput Repay Amount: \33[0m').strip()
        if len(repay_amount) == 0:continue
        if repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
            if new_balance:
                print('\33[42;1mNew Balance is %s : \33[0m' %new_balance['balance'])
            back_flag = False
        else:
            print('\33[31;1m%s is not a valid amount,only accept integer : \33[0m' %repay_amount)


def withdraw(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    print('Balance Info'.center(50, '-'))
    print(u'''
        余额：   %d
        ''' % account_data['balance'])
    back_flag = True
    while back_flag:
        withdraw_amount = input('\33[33;1mInput Withdraw Amount: \33[0m').strip()
        if len(withdraw_amount) == 0: continue
        if withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('\33[42;1mNew Balance is %s : \33[0m' % new_balance['balance'])
            back_flag = False
        else:
            print('\33[31;1m%s is not a valid amount,only accept integer : \33[0m' % withdraw_amount)


def transfer():
    pass


def pay_check():
    pass


def logout(acc_data):
    exit()


def interactive(acc_data):
    print('Bank ATM'.center(50, '-'))
    menu = u'''\33[32;1m
    1、  账户信息
    2、  还款
    3、  取款
    4、  转账
    5、  账单
    q、  退出
    \033[0m
    '''
    menu_dic = {
        '1': account_info,   #  后面的不能加‘’如 ‘account_info’
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        'q': logout
    }
    exit_flag = True
    while exit_flag:
        print(menu)
        choice = input('>>: ').strip()
        if len(choice) == 0: continue
        if choice in menu_dic:
             menu_dic.get(choice)(acc_data)
        else:
            print('\33[31;1mSelect is not exist !\033[0m')


def run():
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_auth']:
        user_data['account_data'] = acc_data
        interactive(user_data)
