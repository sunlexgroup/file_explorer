# File explorer application
"Веб хранилище файлов".

## Запуск приложения
Для запуска необходимо запустить сервер и клиенское приложение.
### Запуск сервера
Переходим в директорию с сервером.

`cd path/to/file_explorer/backend`

Устанавливаем виртуальное окружение. ***Внимание!*** Приложение написано в среде Python 3.9

`python3 -m venv venv`

Запускаем созданное виртуальное окружение.

`source venv/bin/activate`

Перейдем в директорию file_explorer.

`cd file_explorer`

Устанавливаем все необходимые зависимости в виртуальное окружение.

`pip install -r requirements.txt`

Создаем необходимые миграцию данных в базу.
`python manage.py migrate`

При необходимости использования админки создаем суперпользователя.

`python manage.py createsuperuser`

    Следуем вопросам менеджера создания суперпользователя.

Запускаем сервер

`python manage.py runserver`

В случае удачного запуска вы должны увидеть:

    System check identified no issues (0 silenced).
    March 28, 2021 - 10:44:52
    Django version 3.1.7, using settings 'file_explorer.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

***Внимание!***

*Данный тип запуска подходит исключительно для демонстрации приложения.*

Переходим к запуску клиентского приложения.

### Запуск клиентского приложения
Для запуска приложения у вас должен быть установлен node.js

Переходим в директорию frontend

`cd path/to/file_explorer/frontend/`

Выполним установку всех необходимых зависимостей, и запустим приложение.

```
npm install

npm run serve
```

## Использование
Откройте браузер и введите в адресной строке: http://localhost:8080/

Запустится приложение.

