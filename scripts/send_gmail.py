import gmail
import os

user_name = 'atos990@gmail.com'
password  = 'Atos1015'

def do_send(program):
    client = gmail.GMail(user_name, password)

    message = gmail.Message(u'サブジェクト：こんにちは世界', to=user_name, text=u'ボディ：これはテストメッセージです')
    try:
        # client.send(message)
        print('test')
    except Exception as e:
        raise e

    client.close()

    return True