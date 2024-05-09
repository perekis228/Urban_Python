import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and hash(password) == user.password:
                self.current_user = user
                print('Вы успешно вошли в акканут\n')
                break

    def register(self, nickname, password, age):
        flag = False
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                flag = True
                break
        if not flag:
            self.users.append(User(nickname, password, age))
            print('Вы успешно зарегистрировались')
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта\n')

    def add(self, *new_videos):
        for new_video in new_videos:
            have = False
            for old_video in self.videos:
                if old_video.title == new_video.title:
                    have == True
                    break
            if not have:
                self.videos.append(new_video)
                print('Видео добавлено')
        print()

    def get_videos(self, search_word):
        get = []
        search_word = str(search_word)
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                get.append(video.title)
        print(get, '\n')

    def watch_video(self, cur_title):
        for video in self.videos:
            if video.title == cur_title:
                if self.current_user == None:
                    print("Войдите в аккаунт чтобы смотреть видео")
                elif self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(video.time_now, video.duration + 1):
                        min = i // 60
                        sec = i % 60
                        if min < 10 and sec < 10:
                            print(f'0{min}:0{sec}')
                        elif min < 10 and sec >= 10:
                            print(f'0{min}:{sec}')
                        elif min >= 10 and sec < 10:
                            print(f'{min}:0{sec}')
                        elif min >= 10 and sec >= 10:
                            print(f'{min}:{sec}')
                        time.sleep(1)
                    video.time_now = 0
                    print("Конец видео")
                break

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(str(password))
        self.age = int(age)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print('-'*50)

# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')
print('-'*50)

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
print('-'*50)

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)
print('-'*50)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
