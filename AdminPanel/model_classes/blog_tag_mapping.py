from django.db import models


class BlogTagMapping(models.Model):

    blog_id = models.IntegerField(null=False)
    tag_ids = models.IntegerField(null=False)
    active = models.BooleanField(null=False, default=1)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    

    class Meta:
        managed = True
        db_table = 'blog_tag_mapping'
