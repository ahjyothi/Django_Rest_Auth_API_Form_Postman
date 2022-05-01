from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from BlogApp.models import BlogPost
from rest_framework.response import Response
from BlogApp.serializer import BlogPostSerializer
# Create your views here.

# @api_view()
# @permission_classes([AllowAny])
# def index(request):
#     return Response({"message": "Hello, Jyothi!"})



@csrf_exempt
def BlogsView(request):
    if request.method == 'GET':
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogPostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def BlogView(request, nm):
    try:
        blog = BlogPost.objects.get(id=nm)
    except BlogPost.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogPostSerializer(blog, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        blog.delete()
        return HttpResponse(status=204)