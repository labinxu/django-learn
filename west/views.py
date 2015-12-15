from django.shortcuts import render
from django.http import HttpResponse
from west.models import Character



def staff(request):
    staff_list = Character.objects.all()
    staff_str = map(str,staff_list)
    return HttpResponse("" + ' '.join(staff_str) + "")


def first_page(request):
    return HttpResponse("Hello West")
