#Wagtail CMS BLOG Sample 


Cooked Heroku deploy

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/dani4kor/wagtail-heroku)

## USAGE
Deploy this guy, then git clone locally:

```
$ heroku git:clone -a your-heroku-app-name
$ cd your-heroku-app-name
$ git remote add origin https://github.com/Dani4kor/wagtail-heroku
$ git pull origin master
```
Now you have the code for the deployed application and you can make changes to it locally and deploy it back to Heroku.

```
$ git add .
$ git commit -am "Heroku commit"
$ git push heroku master

```



Example
----------
- Usage steps

`$ heroku run python manage.py createsuperuser`

- Create Blogindexpage -> complete the fields
- Add Childpage Blog page for Blogpageindex -> complete the fields
- Goto https://your-heroku-app-name.herokuapp.com/title-blog-page-index
- Open bottle of Beer, cheers


Notice
----------

For productions builds need to provide Django SECRET KEY and another security or static compresson.
Some information you can find on 
* [heroku-django-cookbook](https://github.com/nigma/heroku-django-cookbook)
* [watail heroku deploy](https://wagtail.io/blog/deploying-wagtail-heroku)



http://docs.wagtail.io/en/v1.7/getting_started/tutorial.html








