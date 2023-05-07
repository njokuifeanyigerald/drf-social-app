from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from .forms import SignupForm



@api_view(['GET'])
def me(request):
    context = {
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'gender': request.user.gender,
        'country': request.user.country,
        'phone_number': request.user.phone_number
    }
    # return Response(context, status=status.HTTP_200_OK)
    return JsonResponse(context)
    


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        "gender": data.get('gender'),
        "phone_number": data.get('phone_number'),
        "country": data.get('country'),
        'password1': data['password1'],
        'password2': data.get('password2')
        # "gender", "phone_number" , "country",
    })
    print(form.data)

    if form.is_valid():
        form.save()
        message = form.data
        # else:
        #     message = 'password does not match'
    else:
        return JsonResponse(form.errors)

    return JsonResponse({"status": message})
