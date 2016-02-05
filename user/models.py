from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    role_id = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)

    def __unicode__(self):
        return self.name


class Role(models.Model):
    role_id = models.CharField(max_length=20)
    role_title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.role_title
