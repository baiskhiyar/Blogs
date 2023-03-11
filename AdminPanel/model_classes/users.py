from django.db import models


class Users(models.Model):

    name = models.CharField(max_length=64, null=False)
    username = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False)
    mobile_no = models.CharField(max_length=64, null=False)
    active = models.BooleanField(default=True, null=False)
    password = models.CharField(max_length=64, null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    

    class Meta:
        managed = True
        db_table = 'users'
