from rest_framework.views import APIView
from AdminPanel.models import Users
from django.http import JsonResponse
from django.forms.models import model_to_dict


class UsersView(APIView):

    def get(self, request):
        all_users = Users.objects.filter(active=1)
        result = []
        for user in all_users:
            result.append(model_to_dict(user))
        return JsonResponse({'data': result})
    
    def post(self, request):
        data = request.data
        name = data.get('name')
        username = data.get('username')
        username_exist = Users.objects.filter(username=username).first()
        if username_exist:
            return JsonResponse({'data' : 'Username is already taken!'})
        email_exist = Users.objects.filter(email=email).first()
        if email_exist: 
            return JsonResponse({'data':'Email is already taken!'})
        email = data.get('email')
        mobile_no = data.get('mobile_no')
        mobile_no_exist = Users.objects.filter(mobile_no=mobile_no).first()
        if mobile_no_exist: 
            return JsonResponse({'data':'Email is already taken!'})
        active = data.get('active')
        password = data.get('password')

        Users.objects.create(name=name, username=username, email=email, mobile_no=mobile_no, active=active, password=password)

        return JsonResponse({'data': True})
    
    def put(self, request):

        data = request.data
        user_id = data.get('user_id')
        user = Users.objects.filter(id=user_id)
        if not user:
            return JsonResponse({'data': 'User not found!'})
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        mobile_no = data.get('mobile_no')
        active = data.get('active')
        password = data.get('password')

        Users.objects.update(name=name, username=username, email=email, mobile_no=mobile_no, active=active, password=password)

        return JsonResponse({'data': 'User details updated successfully!'})
