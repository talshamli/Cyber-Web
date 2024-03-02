# Cyber Project

Welcome to the Cyber Project repository!

## About

This project is a Django-based web application designed for showing examples of XSS attacks and Sql injections.
The application is a user register system which registers new users and lets them add customers to a customer list. 
This project has two branches one is vulnrable to all the attacks mentioned above and one handles them and prevents them.
This branch is the vulnerable branch.
## Getting Started

To get a local copy of this project up and running, follow these simple steps.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- Django

### Clone the Repository

```bash
git clone -b vulnerable https://github.com/roeelq323/Cyber-Project.git
```

# Navigate to the Project Directory
```bash
cd Cyber-Project
```
#Create and Activate a Virtual Environment
```bash
# Create a virtual environment named 'env'
virtualenv env
# or if the first one dosent work
python -m venv env
```
# Activate the virtual environment
```bash
env\Scripts\activate.bat        # For Windows
source env/bin/activate          # For Unix/Linux
```
# Install Dependencies
```bash
pip install -r requirements.txt
```
# Connecting to your Database
Go to into Cyber-Project/mysite/mysite/settings.py and open it.
then search for the DATABASES setting and enter your database information.
after that run the following commands:
```bash
cd mysite
# these commands will create the necessary tables in your database:
python manage.py makemigrations
python manage.py migrate
```
# Run the Project
```bash
python manage.py runserver
```
Once the server is running, you can access the application by visiting http://localhost:8000 in your web browser.
# Usage
if you are trying to demonstrate an XSS attack you can do the following:

while logged in click the add customer button and then write in one of the fields an html code for exmaple:
<script>alert("you are hacked")</script>
this should when submitting make an alert everytime the table is opened. 

if you are trying to demonstrate an Sql injection you can do the following:

1. In the login menu you can enter in the username input: ' OR 1=1; -- this will let you login without entering a password.
2. In the register menu you can enter in the username input: ','','','','','','0','1'); --  this will make a new user will with the values you put between the comas without checking for any malicious code.
3. In the add customer menu you can do the same as register and create a customer with any data you want.

