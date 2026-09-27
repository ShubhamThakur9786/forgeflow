from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
# Create your views here.


# def hello(request):

#     user_agent = request.headers.get("User-Agent")

#     name = request.GET.get("name", "guest")

#     return HttpResponse(
#         # f"Method {request.method}"
#         # f"User-Agent {user_agent}"
#         # f"Name {name}"
#     )

# def user_details(request, id):
#     return HttpResponse(
#         f"User_id {id}"
#     )

def proj_demo(request):
    data = {
        "id": 1,
        "name": "shubham",
        "age": 22
    }
    return JsonResponse(data)