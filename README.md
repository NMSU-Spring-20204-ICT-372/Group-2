git clone https://github.com/ICT-372-Spring-2024/django-lms.git

cd django-lms

python -m venv venv

source venv/Scripts/activate

pip install django

cd django-lms/

python manage.py makemigrations lms
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver