import pymysql

def mysqlconnect():
    dataBase = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'root1',
        port = 3307

    )

    cursorObject = dataBase.cursor()

    cursorObject.execute('CREATE DATABASE crm_db')

    dataBase.commit()

    print('All Done!')

    dataBase.close()

if __name__ == '__main__':
    mysqlconnect()


