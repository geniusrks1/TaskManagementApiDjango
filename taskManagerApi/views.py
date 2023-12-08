from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("home page requested")
    task=['a','b','c']
    return JsonResponse(task, safe=False)