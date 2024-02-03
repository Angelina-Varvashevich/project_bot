# Телеграмм-бот для улучшения качества фотографий
  
### О проекте
Телеграмм-бот на основе aiogram.  
Для обработки фотографий использован GFPGAN, предназначенный для реставрации лиц.

### Функционал бота
- По команде /upscale_image происходит обработка отправленного фото, после чего присылается обработанное фото.
- Реакция на сообщения пользователей любого содержания.
- Предусмотрены команды /start и /help для более понятного взаимодействия с ботом.

### Сборка проекта локально
- Необходимо склонировать репозиторий,
- создать .env файл по примеру .env.example, подставив токен своего бота,
- установить необходимые зависимости с помощью команды pip install -r requirements.txt,
- после чего запустить app.py (python app.py)

___В случае возникновения ошибки зайдите в venv/lib/site-packages/basicsr/data/degradations.py и 8 строку замените на from torchvision.transforms.functional import rgb_to_grayscale___  

___Обработка первого фото может занять значительное время, тк во время него подгружаются модели для обработки.___

### __Бот доступен в телеграмм @upscaler_dls_bot. Обработка фото занимает +-5 минут (в некоторых случаях больше).__
  
  
__Ниже приведены примеры взаимодействия с ботом, а также примеры обработки некоторых фотографий:__
![image](https://github.com/Angelina-Varvashevich/project_bot/assets/90001649/24293f80-ea22-47df-99e5-3c8401475fcf)  

![image](https://github.com/Angelina-Varvashevich/project_bot/assets/90001649/f8a5bb41-ea45-4f08-943a-3a9e0ccb8acd)  

![image](https://github.com/Angelina-Varvashevich/project_bot/assets/90001649/e8fed40e-2568-42b2-b17c-e14523040857)  

![image](https://github.com/Angelina-Varvashevich/project_bot/assets/90001649/3a2e708f-d3e2-4a3b-a21c-5065cbb79bab)



  
