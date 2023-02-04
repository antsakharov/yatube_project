# yatube_project

## Описание проекта: 

•	**Назначение:** 

Социальная сеть в которой реализована возможность публикации личных дневников. 

•	**Функции:** 

1. Создание собственной страницы
2. Просмотр всех записей автора
3. Пользователи могут заходить на чужие страницы, подписываться на других авторов и комментировать их записи
4. Автор может выбрать имя и уникальный адрес для своей страницы
5. Записи можно отправить в группу и посмотреть в ней записи разных авторов

•	**Цель выполнения проекта:**

Практика работы с фреймворком Django,БД,Админ-панелью

•	**Стек:**

Python 3.7
Django 2.2.19
SQLite
pytest

## Инструкция по развёртыванию проекта

•	**Клонируйте репозиторий:**

```csharp 
git clone git@github.com:antsakharov/yatube_project.git
```

•	**Установите и активируйте виртуальное окружение:**

**для Linux и MacOS**

```csharp 
python3 -m venv venv
```

**для Windows**

```csharp 
python -m venv venv
```

```csharp 
source venv/bin/activate
```

```csharp 
source venv/Scripts/activate
```

•	**Установите зависимости из файла requirements.txt:**

```csharp 
pip install -r requirements.txt
```
•	**Создайте и выполните миграции:**

```csharp 
python manage.py makemigrations
```

```csharp 
python manage.py migrate
```

