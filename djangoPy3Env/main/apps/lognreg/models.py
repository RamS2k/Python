from django.db import models
import re, bcrypt
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class PersonManager(models.Manager):
    def person_val(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        if len(postData['email']) < 1:
            errors["email"] = "Please enter an email!"
        elif not emailRegex.match(postData['email']):
            errors["email"] = "Please enter a valid email!"
        if len(postData['password']) < 7:
            errors["password"] = "Passwords must be at least 7 characters!"
        elif postData['password'] != postData['pass_conf']:
            errors["password"] = "Passwords must match!"
        return errors

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PersonManager()