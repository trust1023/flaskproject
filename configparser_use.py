import configparser

if __name__ == "__main__":
    cf = configparser.ConfigParser()
    filename = cf.read(['test.ini','test.cfg'])
    print(filename)
    sec = cf.sections()
    print(sec)
    username = cf.get('mysql','username')
    print(username)
    password = cf.get('mysql', 'password')
    print(password)