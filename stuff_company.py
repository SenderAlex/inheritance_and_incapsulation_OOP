class User():
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'


    def get_user_id(self):
        return self.__id

    def get_user_name(self):
        return self.__name


class Admin(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name)
        self.__password = password

    def add_user(self, user_id, user_list, name, password):
        if self.__password == password:
            print(f'Вы зашли от имени администратора и Вы можете добавить в базу работника')
            if any(user.get_user_id() == user_id for user in user_list):
                print(f'Работник с именем {name} уже зарегистрирован')
            else:
                user = User(user_id, name)
                user_list.append(user)
                print(f'Работник с именем {user.get_user_name()} успешно зарегестрирован')
        else:
            print(f'Вы ввели не верный пароль')


    def remove_user(self, user_id, user_list, password):
        if self.__password == password:
            print(f'Вы зашли от имени администратора. Теперь Вы можете удалить из базы работника')
            for user in user_list:
                if user.get_user_id() == user_id:
                    user_list.remove(user)
                    print(f'Пользователь с именем {user.get_user_name()} удален из базы')
        else:
            print(f'Вы ввели не верный пароль')

    def show_stuff_list(self, user_list):
        for user in user_list:
            print(f'{user.get_user_id()}. {user.get_user_name().capitalize()}')

list = []

admin = Admin(1, 'Alex', 'password')
admin.add_user(2, list, 'Michael', 'password')
admin.add_user(3, list, 'Maxim', 'password')
admin.add_user(4, list, 'Katherine', 'password')
admin.show_stuff_list(list)
admin.remove_user(2, list, 'password')
admin.show_stuff_list(list)




