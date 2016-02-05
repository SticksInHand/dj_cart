from django.shortcuts import render
from user.models import Users
from django.http import Http404
# Create your views here.


def user(request, user_id):
    try:
        _post = Users.objects.get(user_id=user_id)
    except Users.doesNotExist:
        return Http404
    
    return render(request, 'user.html', _post=_post)

