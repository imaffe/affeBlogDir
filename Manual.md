## Manual For AffeBlog Deployment

#### How to configure local settings after cloning pycharm project from github?
1. configure your virtual environment
2. runserver and get to your administration site
3. if you use pycharm virtual env, you should run cmd in pycharm terminal


#### How to add components to django blog?


##### URLS

- direct URL :
in the main url.py, assign an url pattern to the absolute location in the project using a string, for example
``` python
urlpatterns = {
    url('admin/',admin.site.urls),
    url('posts/',"posts.views.post_home")
    # in a pattern <appname>.views.<function>
    
    # why we must use string rather than the first row representation?
    #
    
}
```

- using an indirect/hierarchy  URL (in app url)


- regular expression practice


#### Response and Render in view

- get objects in Database.
- put them to dictionaries to be applied to templates
#### Why changes on source code didn't apply?
because the django didn't recognize the source code, and act to some other thing it is used. So we


##### Models 
Model in django can be viewed as a database table, only that it can be easily accessed by both view and controller(this convenience is provided by django, that's what django does).

##### Views 
View is like the controller in MVC design patterns. In view


##### Admin sites
In your subdirectory, create an admin.py and register according to the template admin.site

##### Deploy to remote server

first we need to check re github repo structure, in case we contained something we didn' need at all, this requires us to add .git ignore to the github repo
