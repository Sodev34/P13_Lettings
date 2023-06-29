from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur
# quis velit. Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in
# faucibus orci luctus et ultrices posuere cubilia curae; Cras eget
# scelerisque
def index(request):
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
