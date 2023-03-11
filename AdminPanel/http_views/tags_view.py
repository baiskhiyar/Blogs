from rest_framework.views import APIView
from AdminPanel.models import Tags
from django.http import JsonResponse
from django.forms.models import model_to_dict

class TagsView(APIView):

    def get(self, request):
        all_tags = Tags.objects.filter(acitve=1)
        result = []
        for tag in all_tags:
            result.append(model_to_dict(tag))
        return JsonResponse({'data':result})
    
    def post(self, request):
        data = request.data
        name = data.get('name')
        tag_exist = Tags.objects.filter(name=name).first()
        if tag_exist:
            return JsonResponse({'data': 'Tag with same name already exist. Try with different name!'})
        Tags.objects.create(name=data.get('name'))
        return JsonResponse({'data': 'Tag created successfully!'})
    
    def put(self, request):
        data = request.data
        tag_id = data.get('tag_id')
        tag_data = Tags.objects.filter(id=tag_id).first()
        if not tag_data:
            return JsonResponse({'data':'Tag does not exist!'})
        name = data.get('name')
        if tag_data.name != name:
            name_taken = Tags.objects.filter(name=name).first()
            if name_taken:
                return JsonResponse({'data':'Name already taken!'})
            tag_data.name = name
            tag_data.save()
        return JsonResponse({'data':'Tag Details updated successfully!'})
