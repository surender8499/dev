TMS(Task Management System) This is a simple web application for managing tasks. The application allows users to create, update, delete, and view tasks.

Setup Instructions Prerequisites Python 3.x Git

Clone the Repository git clone https://github.com/your-username/dev.git cd TMS

Set Up Virtual Environment python3 -m venv .venv source .venv/bin/activate # On Windows, use .venv\Scripts\activate

here in these we have django.auth for user authentication and we have utilized django.decorator for login page to check before accesing dashboard the user has to login.

Install Dependencies pip install -r requirements.txt

Apply Database Migrations python manage.py migrate

Run the Application python manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser.

Usage
Access the Homepage : http://127.0.0.1:8000/
Access the register page : http://127.0.0.1:8000/register
Access the dashboard : http://127.0.0.1:8000/dashboard
Access the Login Page : http://127.0.0.1:8000/my-login
Access the task list: http://127.0.0.1:8000/view-tasks
Create a new task: http://127.0.0.1:8000/create-task
Update a task: http://127.0.0.1:8000/update-task/id/
Delete a task : http://127.0.0.1:8000/delete-task3/
Additional Notes Make sure to deactivate the virtual environment after using the application: deactivate

For production deployment, configure your web server (e.g., Nginx, Apache) and use a production-ready database.

task_management/README.md at main · surender8499/task_management
