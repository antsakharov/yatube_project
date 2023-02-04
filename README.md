# yatube_project

## Описание проекта: 

•	**Назначение:** 

Первая версия социальной сети для публикации личных дневников. 

•	**Реализованный функционал:** 

1. Созданны модели групп и постов
2. Создана админ-панель
3. Добавленны шаблоны и стили

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

