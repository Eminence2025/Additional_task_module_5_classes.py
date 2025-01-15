class DataBase():
    def __init__(self):
        self.datausers = {}
        self.datavideos = {}
        
        
    #def add_user(self, nickname, password):
    #    self.data[nickname] = password 
#    def __hasattr__(self)

'''
Каждый объект класса User должен 
обладать следующими атрибутами и методами:

Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
'''

class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
 
      
    
'''
Каждый объект класса Video должен обладать следующими атрибутами и методами:

Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
'''
class Video():
    def __init__(self, title, duration, time_now =0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        #return self.title, self.duration, self.time_now, self.adult_mode

'''
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:

1.  Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    '''
class UrTube():
    current_user = None
    #users = []
    
    
    
    '''
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user
    '''
    '''
    2. Метод log_in, который принимает на    себя         вход аргументы: nickname, password и             пытается найти пользователя в users с         такими же логином и паролем. Если             такой пользователь существует, то                 current_user меняется на найденного.             Помните, что password передаётся в виде     строки, а сравнивается по хэшу.
    '''    
    def log_in(self, nickname, password):
        if nickname in database.datausers.keys() and database.datausers[nickname][0] == password:
            
            print('пользователь найден') 
                
            UrTube.current_user = nickname
            print(UrTube.current_user, 'UrTube.current_user')
        else: print('пользователь не найден')
    
    '''
    3. Метод register, который принимает три        аргумента: nickname, password, age, и             добавляет пользователя в список, если         пользователя не существует (с таким же         nickname). Если существует, выводит             на экран: "Пользователь {nickname}             уже существует". После регистрации,             вход выполняется автоматически.
    '''
    def register(self, nickname, password, age):
        user = User(nickname, password, age)    
        #print(user.age)  
        
        if user.nickname not in list(database.datausers.keys()):
            database.datausers[nickname] = (hash(password), age)
            #автоматический вход
            UrTube.log_in(self, user.nickname, user.password)
            
        else: 
            print(f'пользователь {nickname} уже существует')
            
#        print(database.datausers)
#        print(UrTube.current_user)
    '''
    Метод log_out для сброса текущего   
     пользователя на None.
    '''
    def log_out(self):
        self.current_user = None
    '''
    5. Метод add, который принимает
     неограниченное кол-во объектов класса
     Video и все добавляет в videos, если с
     таким же названием видео ещё не
     существует. В противном случае ничего
     не происходит.
    '''
    def add(self, *args):
        for i in range(len(args)):
            database.datavideos[args[i].title] = ( args[i].duration, args[i].time_now, args[i].adult_mode)
       # print(database.datavideos, 'database.datavideos')
        
    '''
    6. Метод get_videos, который принимает
     поисковое слово и возвращает список
     названий всех видео, содержащих
     поисковое слово. Следует учесть, что
     слово 'UrbaN' присутствует в строке
     'Urban the best' (не учитывать регистр).     
    '''
    def get_videos(self, find_word):
        lists=[]       
        for i in list(database.datavideos.keys()):
           if find_word.lower() in i.lower():
               lists.append(i)
        return lists
    
    '''
    7. Метод watch_video, который принимает
     название фильма, если не находит
     точного совпадения(вплоть до пробела),
          то ничего не воспроизводится, если
     же находит - ведётся отчёт в консоль на
     какой секунде ведётся просмотр. После
     текущее время просмотра данного
     видео сбрасывается.

    Для метода watch_video так же
     учитывайте следующие особенности:

    1.Для паузы между выводами секунд
     воспроизведения можно использовать
     функцию sleep из модуля time.
    2. Воспроизводить видео можно только
     тогда, когда пользователь вошёл в
     UrTube. В противном случае выводить в
     консоль надпись: "Войдите в аккаунт,
      чтобы смотреть видео"
    3. Если видео найдено, следует учесть,
     что пользователю может быть отказан в
     просмотре, т.к. есть ограничения 18+.
      Должно выводиться сообщение: "Вам
     нет 18 лет, пожалуйста покиньте
     страницу"
    4. После воспроизведения нужно
     выводить: "Конец видео"
    '''
    def watch_video(self,name_movie):
        if name_movie not in list(database.datavideos.keys()):
            print('видео не найдено')
        elif UrTube.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        
        elif database.datausers[UrTube.current_user][1] < 18 :
            #print(database.datavideos)
            if database.datavideos[name_movie][2] == True:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            
        elif database.datausers[UrTube.current_user][1] > 18 :
           print()
           from time import sleep
           for i in range(database.datavideos[name_movie][0]+1):                  
                  print(i, end=' ')
                  #sleep(0.5)
           print('конец видео')
           
              
                 
                       
database= DataBase()    
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
#print(database.datavideos)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)    
#print(database.datavideos)    
    
# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))    
    
# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')    

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')

