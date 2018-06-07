from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from xujia.models.article.article import Article
from markdown2 import Markdown
import logging


def index(request):
    user_id = request.session['user_id'] or 1
    articles = Article.get_list(user_id)
    md = Markdown()
    for article in articles:
        article['body'] = md.convert(article['body'])
    return render(request, 'article/index.html', {'articles': articles})


def publish(request):
    return render(request, 'article/publish.html')

