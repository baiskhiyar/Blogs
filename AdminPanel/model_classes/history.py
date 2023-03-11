from django.db import models


class History(models.Model):

    searched_item = models.CharField(max_length=64, null=False)
    user_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    

    class Meta:
        managed = True
        db_table = 'history'
