* **Django 安裝過程**

```shell
apt update
apt upgrade
apt install virtualenv

virtualenv VENV
source VENV/bin/activate

pip install django

django-admin startproject tpcu
cd tpcu
django-admin startapp mainsite
```
* **建立templates 和 static Folder 找到TPCU專案底下的 Settings .py**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainsite', <-- 新增剛剛創建的App名稱
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], <-- 加入templates 資料夾
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'zh-Hant' <-- 改為繁體中文

TIME_ZONE = 'Asia/Taipei' <-- 時間改為亞洲台北

STATIC_URL = '/static/'
STATICFILES_DIRS = ['static'] <-- 設定 static 資料夾路徑
```

* **到TPCU專案底下找到urls .py**

```python
path('',views.get_time),
```

* **到TPCU專案底下尋找剛剛創建的APP名稱找到他的views .py**

```python
from django.shortcuts import render
from .models import Post
import datetime

# Create your views here.

def get_time(request):
    return render(request,'index.html',{
        'time': datetime.datetime.now
    })
```

* **到templates資料夾，新增一個文件叫做 index.html (先打一個驚嘆號 + Tab 可以直接創造基本網頁)**
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
</head>

<body>
    {{ time }}
</body>

</html>
```

* **回到終端機底下輸入指令，開啟localhost:8000**

```shell
python manage.py runserver
```