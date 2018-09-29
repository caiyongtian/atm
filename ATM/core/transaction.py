
from conf import setting
from core import accounts

def make_transaction(log_obj,account_data,trans_type,amount,**other):
    '''
    deal all the user transaction
    :param log_obj
    :param account_data
    :param trans_type
    :param repay_amount
    :param other
    :return : None
    '''
    amount = float(amount)
    if trans_type in setting.TRANSACTION_TYPE:
        interest = amount * setting.TRANSACTION_TYPE[trans_type]['interest']
        old_balance = account_data['balance']
        if setting.TRANSACTION_TYPE[trans_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif setting.TRANSACTION_TYPE[trans_type]['action'] == 'minus':
            new_balance = old_balance - amount -interest
            if new_balance < 0:
                print('\33[31;1mYour Credit [%s] is not enough for this transaction\033[0m'% account_data['id'])
                return
        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        log_obj.info('account： %s,action: %s,amount: %s,interest: %s' %(account_data['id'],trans_type,amount,interest))
