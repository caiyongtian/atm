import json


acc_dict = {
    'id': '000000',
    'password': 'admin123',
    'name': '管理初始化',
    'enroll_date': 'Fri Sep 28 18:10:26 2018',
    'expire_date': 'Fri Sep 28 18:10:26 2020',
    'status': 0 #0 = normal,  1 = locked, 2 = disabled
}
with open('accounts/000001.json','w') as f:
    json.dump(acc_dict,f)