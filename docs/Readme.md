# Use the below instructions while deploying in the ORACLE CLOUD

**NOTE: - The following commands are compleletly with respect to linux based OS (ubuntu)**

## Step 1: -

In the file **settings.py** in the folder **django_project**
In **line 28**, the following should be there,
```
  ALLOWED_HOSTS = ['*']
```
## Step 2: -

Type the commands listed below,
```
  source env/bin/activate
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8000
```  

With this the web application can be accessed outside the OCI with the _**IP ADDRESS**_:_**8000**_ typed in the url of any device in the web browser. 
where _**IP ADDRESS**_ is the **PUBLIC IP ADDRESS** of the OCI
