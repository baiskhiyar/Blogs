from rest_framework.views import APIView
from AdminPanel.models import Blogs
from django.http import JsonResponse
from django.forms.models import model_to_dict

class BlogsView(APIView):

    def get(self, request):
        data = request.data
        blog_id = data.get('blog_id')
        if blog_id:
            blogs = Blogs.objects.filter(id=blog_id)
        else:
            blogs = Blogs.objects.filter()
        result = []
        for blog in blogs:
            result.append(model_to_dict(blog))
            
        return JsonResponse({'data': result})
    
    def post(self, request):
        pass
    def put(self, request):
        pass
