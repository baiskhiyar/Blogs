from django.db import models


class Tags(models.Model):

    name = models.CharField(max_length=64, null=False)
    acitve = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    
    class Meta:
        managed = True
        db_table = 'tags'
