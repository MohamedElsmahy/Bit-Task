# Bit68 Task

Django APIs and API Test Cases .

# Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/MohamedElsmahy/Bit-Task.git
```
Then open cmd and run this command to create virtual environement,
If you want to know more about [virtualenv](https://virtualenv.pypa.io/en/latest/) :

```bash
virtualenv venv
```
Then activate it using :

```bash
.\venv\Scripts\activate
```
# After Activation 

Install the requirements:

```bash
pip install -r requirements.txt
```
# Connect to PostgreSQl Database
before apply migrations you need to connect with your postgreSQl database pgAdmin4 and create database .

in settings.py :

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Your Database Name',
        'USER': 'Your PostgreSQL User',
        'PASSWORD': 'Your PostgreSQL Password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Apply the migrations :

```bash
python manage.py makemigrations
```
then migrate :

```bash
python manage.py migrate
```

Finally, run the development server :

```bash
python manage.py runserver
```

## Usage

To verify that the API is working, you can use postman to test requests, If you want to know more about [postman](https://www.postman.com/) :

**Registeration API test :**

![Screenshot Registeration](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/registeration.PNG)

**Login API with simple JWT test :**

![Screenshot Login](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/login.PNG)

**Bearer Token Autherization to APIs which need access token :**

![Screenshot Bearer](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/Bearer_Token.PNG)

**loged in user can add his products :**

![Screenshot Add_Product](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/Add_Products.PNG)

**Get user data :**

![Screenshot User](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/Get_User.PNG)

**Get user products data :**

![Screenshot User_Products](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/Get_User_Products.PNG)

**All users can see all products data :**

![Screenshot User_Products](https://github.com/MohamedElsmahy/Bit-Task/blob/main/screenshots/All_Products.PNG)