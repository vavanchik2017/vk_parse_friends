import vk_api
import getpass


z = 0
login = input('Введите логин \n') 
password = getpass.getpass('Введите пароль \n')
usid = input('Введите id пользователя \n')

vk_session=vk_api.VkApi(login,password) #Авторизация
try:
    vk_session.auth()
except vk_api.AuthError as error_msg: #Возврат ошибки, в случае неверных данных
    print(error_msg)

vk = vk_session.get_api() #Получаем API вк
resp = vk.friends.get (user_id=usid, order='name') #Входящие параметры для запроса
if resp['items'] and resp['count']:
    output= open("friends"+usid+".txt","w",encoding="utf-8") #Создание файла для результатов
    for i in range(0,(resp['count'])):
        frnds ="\n vk.com/"+str(resp['items'][z]) #Собираем ссылки
        output.write(frnds)
        z= z + 1
    output.close()
print ('PROFIT!1')
