from django.shortcuts import render


def index(request):
    return render(request, 'exampleURL/index.html', locals())


def special_case_2009(request):
    return render(request, 'exampleURL/special_case_2009.html', locals())


def year_archive(request, year):
    return render(request, 'exampleURL/year_archive.html', locals())


def month_archive(request, year, month):
    return render(request, 'exampleURL/month_archive.html', locals())


def article_detail(request, year, month, slug):
    return render(request, 'exampleURL/article_detail.html', locals())


def article_detail_converters(request, year, month, slug):
    return render(request, 'exampleURL/article_detail_converters.html', locals())


def article_detail_regexp(request, year, month, slug):
    return render(request, 'exampleURL/article_detail_regexp.html', locals())


def page(request, num=73):
    return render(request, 'exampleURL/page.html', locals())


def parameter_passing(request, param1, param2):
    return render(request, 'exampleURL/parameter_passing.html', locals())