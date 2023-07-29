from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(r):
    return HttpResponse("<h1>Hi Its a Deployment_29Jul Project , We are deploying it using AWS, jenkins, Docker, Git</h1>")