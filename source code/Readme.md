# Follow the instructions for the Feature of _reset_ for the web application

## Step 1: - 

- Make sure the user has a **G-MAIL** account with **2-step Verification**.
- Follow the below link if the **G-MAIL** account does not have **2-step Verification**.
```
    https://support.google.com/accounts/answer/185833?hl=en
```

## Step 2: - 

In line **135** and **136**, in the file '**settings.py**', in the folder '**django_project**',

```
    EMAIL_HOST_USER = ''   # type email of your gmail account
    EMAIL_HOST_PASSWORD = ''  # type the password for the SmartAGRI app
```

Make sure to fill these with respective **G-MAIL** account with **2-step Verification**

The above is only for a **single user** __*RESET PASSWORD*__ feature.
The above is not yet applicable for __production level__ as it is currenlty in the __development mode__. *__(It works with 100% accuracy).__*
The above feature can be modified for production level using the documentation in the link given below,

```
    https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth
```

OR

```
    https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views
```
