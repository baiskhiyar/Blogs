from rest_framework.views import APIView
from AdminPanel.models import History
from django.http import JsonResponse
from django.forms.models import model_to_dict

class HistoryView(APIView):

    def get(self, request):
        all_searched_items = list(History.objects.filter().values_list('searched_item', flat=True))
        return JsonResponse({'data': all_searched_items})
    
    def post(self, request):
        data = request.data
        searched_item = data.get('searched_item')
        History.objects.create(searched_item=searched_item)
        return JsonResponse({'data' : True})
    
