# This repo create special for my educating in *async* _/_ *Django* _/_ *aiogram*

### Base step for start project

+ Create virtual environment -> ```python3 -m venv venv_web_app```
+ At first step install all libs from [requirements.txt](requirements.txt) this command -> ```pip install -r requirements.txt```
+ Create ```.env``` file, copy text from [dot_env_template.txt](dot_env_template.txt) -> ```.env```. After you must change parameters for you

### Nice, after this step you need spend few second for next command in this project:
+ ```python manage.py migrate``` - apply migration in database
+ ```python manage.py createsuperuser``` - create super user for django admin