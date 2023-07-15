# api_final yatube_project
## Социальная сеть блогеров
### Описание
Благодаря этому проекту блогерам можно будет публиковать личные дневники.
Пользователи могут подписываться на авторов и кооментировать их записи.
### Технологии
asgiref==3.7.2
atomicwrites==1.4.1
attrs==23.1.0
certifi==2023.5.7
cffi==1.15.1
charset-normalizer==2.0.12
colorama==0.4.6
cryptography==41.0.2
defusedxml==0.7.1
Django==3.2.16
django-filter==23.2
django-templated-mail==1.1.1
djangorestframework==3.12.4
djangorestframework-simplejwt==5.2.2
djoser==2.2.0
idna==3.4
iniconfig==2.0.0
oauthlib==3.2.2
packaging==23.1
Pillow==9.3.0
pluggy==0.13.1
py==1.11.0
pycparser==2.21
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
python3-openid==3.2.0
pytz==2023.3
requests==2.26.0
requests-oauthlib==1.3.1
social-auth-app-django==5.2.0
social-auth-core==4.4.2
sqlparse==0.4.4
toml==0.10.2
urllib3==1.26.16
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
- Выполните миграции

### Примеры запросов API:
- Получить список всех публикаций: /api/v1/posts/
- Получение всех комментариев к публикации: /api/v1/posts/{post_id}/comments/
- Получение списка доступных сообществ: /api/v1/groups/
- Подписки пользователя: /api/v1/follow/
