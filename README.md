**Library Management System (LMS) by Team Tabs vs Spaces**
Welcome to the Library Management System (LMS) developed by Team Tabs vs Spaces! Our team consists of Ajay Bhakta as the Developer, Reagan Davis as the Scrum Master, and Zachary Donnelly (me) as the Product Owner.

**About the Product**
The LMS is a comprehensive solution designed to simplify book inventory management for libraries worldwide. With LMS, libraries can effortlessly track their book inventory, add and delete books, and manage book statuses such as checked out and returned.

**Target Audience**
Our target audience includes various organizations within the library industry, including public and private libraries, bookstores, and book enthusiasts/collectors. These users require a basic yet efficient tool for managing their book inventory effectively.

Stay tuned for updates as we progress towards delivering a robust and efficient Library Management System tailored to meet the needs of libraries worldwide. Thank you for your interest in our project!


**How to download and run the LMS application (Linux Ubuntu User)**

git clone https://github.com/ICT-372-Spring-2024/django-lms.git

sudo apt-get install python3

sudo apt-get install python3-venv

sudo apt install python3-pip

cd django-lms

sudo python3 -m venv venv

source venv/bin/activate 

sudo pip install django

cd django-lms/

sudo python3 manage.py makemigrations lms

sudo python3 manage.py migrate

sudo python3 manage.py createsuperuser

sudo python3 manage.py runserver

You can now access the LMS application by navigating to http://127.0.0.1:8000/ in your web browser.


Thank you again! 
