from rest_framework.views import APIView
from AdminPanel.models import BlogTagMapping
from AdminPanel.models import Blogs
from django.http import JsonResponse
from django.forms.models import model_to_dict

class BlogTagMappingView(APIView):

    def get(self, request):
        data = request.data
        tag_id = data.get('tag_id')
        mapped_blog_ids = list(BlogTagMapping.objects.filter(tag_id=tag_id).values_list('blog_id', flat=True))
        blogs = Blogs.objects.filter(id__in=mapped_blog_ids)
        result = []
        for blog in blogs:
            result.append(model_to_dict(blog))

        return JsonResponse({'data':result})
    
    def post(self, request):
        data = request.data
        tag_id = data.get('tag_id')
        blog_id = data.get('blog_id')
        mapping_exist = BlogTagMapping.objects.filter(tag_id=tag_id, blog_id=blog_id).first()
        if mapping_exist:
            mapping_exist.active=1
            mapping_exist.save()
        else:
            BlogTagMapping.objects.create(tag_id=tag_id, blog_id=blog_id)
        return JsonResponse({'data': True})


    def put(self, request):
        data = request.data
        tag_id = data.get('tag_id')
        blog_id = data.get('blog_id')
        active = data.get('active')
        mapping_exist = BlogTagMapping.objects.filter(tag_id=tag_id, blog_id=blog_id).first()

        if mapping_exist:
            mapping_exist.active=active
            mapping_exist.save()
        else:
            return JsonResponse({'detail':'Blog not mapped with the tag!'})
        
        return JsonResponse({'data':'Updated successfully!'})
