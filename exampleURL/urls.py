from django.urls import path, re_path, register_converter, include

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.TwoDigitMonthConverter, 'mm')

app_name = 'exampleURL'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/2009/', views.special_case_2009, name='special_case_2009'),
    path('articles/<int:year>/', views.year_archive, name='year_archive'),
    path('articles/<int:year>/<int:month>/', views.month_archive,
         name='month_archive'),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail,
         name='article_detail'),

    # use convertor
    path('articles/<yyyy:year>/<mm:month>/<slug:slug>/',
         views.article_detail_converters,
         name='article_detail_converters'),

    # use regexp
    re_path(
        r'^articles/(?P<year>[12][0-9]{3})/(?P<month>0[1-9]|1[0-2])/(?P<slug>[\w-]+)/$',
        views.article_detail_regexp, name='article_detail_regexp'),

    # задание аргументов по умолчанию (views)
    path('blog/', include([
        path('', views.page, name='page1'),
        path('page<int:num>/', views.page, name='page2'),
    ])),

    # передача дополнительных параметров
    path('parameter_passing/', views.parameter_passing, {'param1': 73, 'param2': 37}, name='parameter_passing'),
]
