from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from userapi.serializers import UserSerializer, LoginSerializer
from userapi.models import User

@csrf_exempt
def userAPI(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=id)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    

    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)

class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']
                print(email)
                print(password)
                user = authenticate(email=email, password=password)
                print(user)
                if user is None:
                    return JsonResponse({'message': 'Invalid Credentials'}, status=400)

                refresh = RefreshToken.for_user(user)

                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            }, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
