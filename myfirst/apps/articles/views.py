from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Article


def index(request):
    latest_article = Article.objects.order_by('-pub_date')[:1]
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html',
                  {'latest_articles_list': latest_articles_list, 'latest_article': latest_article})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена...")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена...")
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def article_create(request):
    article_title_creation = str(request.POST.get('article_name'))
    article_text_creation = str(request.POST.get('article_text'))
    image=request.FILES.get('files[]')
    print(image)
    if request.method == 'POST':
        try:
           a = Article(article_title=article_title_creation, arcticle_text=article_text_creation, pub_date=
           timezone.now(), header_image=image)
           a.save()
           answer = "Статья была создана!"
           return render(request, 'articles/article_create.html', {'answer': answer})
        except:
            answer = "Ой, что-то пошло" \
                     " не так..."
            return render(request, 'articles/article_create.html', {'answer': answer})
    answer=''
    return render(request, 'articles/article_create.html', {'answer': answer})
