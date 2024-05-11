git clone https://github.com/ICT-372-Spring-2024/django-lms.git

sudo apt-get install python3

sudo apt-get install python3-venv

sudo apt install python3-pip

cd django-lms

sudo python3 -m venv venv

source venv/bin/activate 

sudo pip install django

cd django-lms/

sudo python manage.py makemigrations lms

sudo python manage.py migrate

sudo python manage.py createsuperuser

sudo python manage.py runserver
