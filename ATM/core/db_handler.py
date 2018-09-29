import os
from conf import setting

def file_db_handle(conn_parms):
    db_path = os.path.join(setting.BASE_DIR,conn_parms['path'],conn_parms['name'])
    return db_path

def db_handler(conn_parms):
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)