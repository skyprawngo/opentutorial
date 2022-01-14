from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]
# Create your views here.

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <h2>Welcome</h2>
        Hello, Django
        <ul>
            <a href="/create/">create</a>
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
        <h2>Welcome</h2>
        Hello, Django
    '''
    return HTTPResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    article = '''
        <form action="/create/">
            <p><input type="text" name="title" placeholder="Title"></p>
            <p><textarea name="body", placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))