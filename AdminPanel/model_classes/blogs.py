from django.db import models


class Blogs(models.Model):

    name = models.CharField(max_length=64, null=False)
    acitve = models.BooleanField(default=True, null=False)
    admin_user_id = models.IntegerField(null=False)
    blog_details = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    

    class Meta:
        managed = True
        db_table = 'blogs'
