from django.http import HttpResponse, JsonResponse
from modelapp.models import Article
from django.forms.models import model_to_dict
from django.db.models import Count


# http://127.0.0.1:8000/api/init_article?PageNo=1&PageSize=4&ArticleType=1
def init_article(r):
    PageNo = int(r.GET.get('PageNo'))
    PageSize = int(r.GET.get('PageSize'))
    ArticleType = int(r.GET.get('ArticleType'))
    if ArticleType != 0:
        RowCount = Article.objects.filter(ArticleType__exact=ArticleType).count()
        lsArticle = list(
            Article.objects.filter(ArticleType__exact=ArticleType)[(PageNo - 1) * PageSize:(PageNo - 1) * PageSize+PageSize].values())
    else:
        RowCount = 0
        lsArticle = []
        lsArtType = list(Article.objects.values('ArticleType').annotate(Count=Count('ArticleType')).order_by())

        for ojbArtType in lsArtType:
            lsArticleWithType = list(
                Article.objects.filter(ArticleType__exact=ojbArtType['ArticleType'])[(PageNo - 1) * PageSize:(PageNo - 1) * PageSize+PageSize].values())
            lsArticle.append(lsArticleWithType)
    rs = {'Code': 200, 'Msg': '',
          'Data': {'DataSet': lsArticle, 'RowCount': RowCount, 'PageNo': PageNo, 'PageSize': PageSize}}
    return JsonResponse(rs, safe=False)
