from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'cms/index.html',{'test':'ulogovan'})
    else:
        return render(request, 'cms/index.html',{'test':'nije ulogovan'})