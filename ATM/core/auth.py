import os
import json
import time
from core import db_handler
from conf import setting

def acc_auth(account,password):
    db_path = db_handler.db_handler(setting.DATABASE)
    account_file = '%s.json'%(os.path.join(db_path,account))
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date']))
                if time.time() > exp_time_stamp:
                    print('\33[31;1mAccount [%s] has expired,please contact the manager !\033[0m' %account)
                else:
                    return account_data
            else:
                print('\33[31;1mAccount ID or Password is incorrect !!\033[0m')
    else:
        print('\33[31;1mAccount [%s] does not exist !\033[0m' %account)

def acc_login(user_data,log_obj):
    retry_count = 0
    while user_data['is_auth'] is False and retry_count < 3:
        account = input('\033[32;1mAccount: \033[0m').strip()
        if len(account) == 0:continue
        password = input('\033[32;1mPassword: \033[0m').strip()
        if len(password) == 0:continue
        auth = acc_auth(account,password)
        if auth:
            user_data['is_auth'] = True
            user_data['account_id'] = account
            return auth
        else:
            retry_count += 1
    else:
        log_obj.error('Account [%s] try more then 3 time,Is locked' %account)
        exit()
