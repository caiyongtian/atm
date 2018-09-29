import os
import json
from core import db_handler
from conf import setting

def load_current_balance(account_id):
    db_path = db_handler.db_handler(setting.DATABASE)
    account_file = '%s.json' % (os.path.join(db_path, account_id))
    with open(account_file,'r') as f:
        acc_data = json.load(f)
        return acc_data


def dump_account(account_data):
    db_path = db_handler.db_handler(setting.DATABASE)
    account_file = '%s.json' % (os.path.join(db_path, account_data['id']))
    with open(account_file,'w') as f:
        acc_data = json.dump(account_data,f)
    return True
