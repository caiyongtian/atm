import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

SEP = os.sep

LOG_LEVEL = logging.INFO
LOG_TYPE = {
    'transaction': 'transactions.log',
    'access': 'access.log'
}

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': os.path.join(BASE_DIR,'db')
}

TRANSACTION_TYPE = {
    'repay': {'action': 'plus','interest': 0},           #还款
    'withdraw': {'action': 'minus','interest': 0.05},    #取款
    'transfer': {'action': 'minus','interest': 0.05},    #转账
    'consume': {'action': 'minus','interest': 0}         #消费
}
